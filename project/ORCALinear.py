import math

class Agent:
    def __init__(self, sim, id, position, neighborDist, maxNeighbors, timeHorizon, timeHorizonObst, radius, maxSpeed, velocity):
        self.sim = sim
        self.id = id
        self.position = position
        self.neighborDist = neighborDist
        self.maxNeighbors = maxNeighbors
        self.timeHorizon = timeHorizon
        self.timeHorizonObst = timeHorizonObst
        self.radius = radius
        self.maxSpeed = maxSpeed
        self.velocity = velocity
        self.prefVelocity = velocity #initially, they might be the same? I dunno lets try and see.
        self.agentNeighbors = []
        self.newVelocity = None
        self.obstacleNeighbors = []
        self.orcaLines = []

    def computeNeighbors(self):
        self.obstacleNeighbors.clear()
        rangeSq = (self.timeHorizonObst * self.maxSpeed + self.radius) ** 2
        self.sim.kdTree.computeObstacleNeighbors(self, rangeSq)

        self.agentNeighbors.clear()

        if self.maxNeighbors > 0:
            rangeSq = self.neighborDist ** 2
            self.sim.kdTree.computeAgentNeighbors(self, rangeSq)


    def linearProgram(self, lines, radius, optVelocity, directionOpt, useExtendedBounds):
        if directionOpt:
            optVelocity = normalize(optVelocity)
            direction = Vector2(optVelocity.y, -optVelocity.x)
            line = Line()
            line.direction = direction
            if useExtendedBounds:
                line.point = optVelocity * 0.5
                line.point -= Vector2(direction.y, -direction.x) * (radius * 2.0)
            else:
                line.point = Vector2(line.direction.y, -line.direction.x) * radius
        elif useExtendedBounds:
            line = Line()
            line.direction = Vector2(0.0, 0.0)
            line.point = Vector2(-optVelocity.y, optVelocity.x).normalize() * radius * 2.0
        else:
            line = Line()
            line.direction = Vector2(-optVelocity.y, optVelocity.x).normalize()
            line.point = Vector2(line.direction.y, -line.direction.x) * radius

        lines.append(line)

        numLines = len(lines)
        lambdaValues = [0.0] * numLines
        direction = Vector2(0.0, 0.0)
        result = Vector2(0.0, 0.0)

        for i in range(numLines):
            if directionOpt or useExtendedBounds:
                lambdaValues[i] = det(lines[i].point - self.position, lines[i].direction)
                direction += lambdaValues[i] * lines[i].direction
            else:
                lambdaValues[i] = det(lines[i].point - self.position, lines[i].direction) / absSq(lines[i].direction)

        if directionOpt or useExtendedBounds:
            result = optVelocity - direction
        else:
            result = optVelocity - (direction / self.timeHorizon)

        result /= numLines

        if not directionOpt and result.length() > radius:
            result = normalize(result) * radius

        return result

    def insertAgentNeighbor(self, agent, rangeSq):
        if self != agent:
            distSq = absSq(self.position - agent.position)
            if distSq < rangeSq:
                if len(self.agentNeighbors) < self.maxNeighbors:
                    self.agentNeighbors.append(AgentNeighbor(agent, distSq))

                    i = len(self.agentNeighbors) - 1
                    while i > 0 and distSq < self.agentNeighbors[i - 1].distSq:
                        self.agentNeighbors[i] = self.agentNeighbors[i - 1]
                        i -= 1

                    self.agentNeighbors[i] = AgentNeighbor(agent, distSq)

                i = len(self.agentNeighbors) - 1

                while i != 0 and distSq < self.agentNeighbors[i - 1].distSq:
                    self.agentNeighbors[i] = self.agentNeighbors[i - 1]
                    i -= 1

                self.agentNeighbors[i] = AgentNeighbor(agent, distSq)

    def insertObstacleNeighbor(self, obstacle, rangeSq):
        nextObstacle = obstacle.nextObstacle
        distSq = distSqPointLineSegment(obstacle.point, nextObstacle.point, self.position)

        if distSq < rangeSq:
            self.obstacleNeighbors.append(ObstacleNeighbor(obstacle, distSq))

            i = len(self.obstacleNeighbors) - 1

            while i != 0 and distSq < self.obstacleNeighbors[i - 1].distSq:
                self.obstacleNeighbors[i] = self.obstacleNeighbors[i - 1]
                i -= 1

            self.obstacleNeighbors[i] = ObstacleNeighbor(obstacle, distSq)

    def update(self):
        self.velocity = self.newVelocity
        self.position += self.velocity * self.sim.timeStep

class AgentNeighbor:
    def __init__(self, agent, distSq):
        self.agent = agent
        self.distSq = distSq

class ObstacleNeighbor:
    def __init__(self, obstacle, distSq):
        self.obstacle = obstacle
        self.distSq = distSq

class Line:
    def __init__(self):
        self.direction = Vector2(0.0, 0.0)
        self.point = Vector2(0.0, 0.0)

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        length = self.length()
        return Vector2(self.x / length, self.y / length)

def det(v1, v2):
    return v1.x * v2.y - v1.y * v2.x

def absSq(v):
    return v.x ** 2 + v.y ** 2

def normalize(v):
    length = v.length()
    return Vector2(v.x / length, v.y / length)

def distSqPointLineSegment(a, b, c):
    aux1 = c - a
    aux2 = b - a
