import torch.nn.functional as F
import torch.nn as nn
import torch

class Actor(nn.Module):
    def __init__(self, state_dim, action_dim, net_width, maxaction):
        super(Actor, self).__init__()

        self.l1 = nn.Linear(state_dim, net_width)
        self.l2 = nn.Linear(net_width, net_width)
        self.l3 = nn.Linear(net_width, action_dim)

        self.maxaction = maxaction

    def forward(self, state):
        a = torch.tanh(self.l1(state))
        a = torch.tanh(self.l2(a))
        a = torch.tanh(self.l3(a)) * self.maxaction
        return a


class Double_Q_Critic(nn.Module):
    def __init__(self, state_dim, action_dim, net_width):
        super(Double_Q_Critic, self).__init__()

        # Critic 1
        self.l1 = nn.Linear(state_dim + action_dim, net_width)  
        self.l2 = nn.Linear(net_width, net_width)
        self.l3 = nn.Linear(net_width, 1)

        # Critic 2
        self.l4 = nn.Linear(state_dim + action_dim, net_width)
        self.l5 = nn.Linear(net_width, net_width)
        self.l6 = nn.Linear(net_width, 1)


    def forward(self, state, action):
        sa = torch.cat([state, action], 1)

        #Forward ReLU activation functions of critic 1 defined here
        q1 = F.relu(self.l1(sa))
        q1 = F.relu(self.l2(q1))
        q1 = self.l3(q1)
        #Forward ReLU activation functions of critic 2 defined here
        q2 = F.relu(self.l4(sa))
        q2 = F.relu(self.l5(q2))
        q2 = self.l6(q2)
        return q1, q2


    def Q1(self, state, action):
        sa = torch.cat([state, action], 1)

        q1 = F.relu(self.l1(sa))
        q1 = F.relu(self.l2(q1))
        q1 = self.l3(q1)
        return q1

"""
This is the function for evaluating the policy.
It seems to perform somewhat better when evaluation is done at
mode than one turn, hence, a default value >1 is given.
"""
def evaluate_policy(env, agent, turns = 3):
    total_scores = 0
    for j in range(turns):
        s, info = env.reset()
        done = False
        while not done:
            # Take deterministic actions at test time
            a = agent.select_action(s, deterministic=True)
            s_next, r, dw, tr, info = env.step(a)
            done = (dw or tr)

            total_scores += r
            s = s_next
    return int(total_scores/turns)




#reward engineering for better training
def Reward_adapter(r):
  
    if r <= -100: r = -10
    return r