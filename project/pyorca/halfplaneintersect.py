"""This module solves 2D linear programming using half-plane intersection.
IMPORTANT: For original implementation, please refer to https://github.com/Muon/pyorca
"""

from __future__ import division

import itertools

from numpy import dot, clip, array, sqrt
from numpy.linalg import det


class InfeasibleError(RuntimeError):
    """Raised if an LP problem has no solution."""
    pass


class Line(object):
    """A line in space."""
    def __init__(self, point, direction):
        super(Line, self).__init__()
        self.point = array(point)
        self.direction = normalized(array(direction))

    def __repr__(self):
        return "Line(%s, %s)" % (self.point, self.direction)


def halfplane_optimize(lines, optimal_point):
    """Find the point closest to optimal_point in the intersection of the
    closed half-planes defined by lines which are in Hessian normal form
    (point-normal form)."""
    # We implement the quadratic time (though linear expected given randomly
    # permuted input) incremental half-plane intersection algorithm as laid
    # out in http://www.mpi-inf.mpg.de/~kavitha/lecture3.ps
    point = optimal_point
    for i, line in enumerate(lines):
        # If this half-plane already contains the current point, all is well.
        if dot(point - line.point, line.direction) >= 0:
            # assert False, point
            continue

        # Otherwise, the new optimum must lie on the newly added line. Compute
        # the feasible interval of the intersection of all the lines added so
        # far with the current one.
        prev_lines = itertools.islice(lines, i)
        left_dist, right_dist = line_halfplane_intersect(line, prev_lines)

        # Now project the optimal point onto the line segment defined by the
        # the above bounds. This gives us our new best point.
        point = point_line_project(line, optimal_point, left_dist, right_dist)
    return point

def point_line_project(line, point, left_bound, right_bound):
    """Project point onto the line segment defined by line, which is in
    point-normal form, and the left and right bounds with respect to line's
    anchor point."""
    # print("left_bound=%s, right_bound=%s" % (left_bound, right_bound))
    new_dir = perp(line.direction)
    # print("new_dir=%s" % new_dir)
    proj_len = dot(point - line.point, new_dir)
    # print("proj_len=%s" % proj_len)
    clamped_len = clip(proj_len, left_bound, right_bound)
    # print("clamped_len=%s" % clamped_len)
    return line.point + new_dir * clamped_len

def line_halfplane_intersect(line, other_lines):
    """Compute the signed offsets of the interval on the edge of the
    half-plane defined by line that is included in the half-planes defined by
    other_lines.

    The offsets are relative to line's anchor point, in units of line's
    direction.

    """
    # We use the line intersection algorithm presented in
    # http://stackoverflow.com/a/565282/126977 to determine the intersection
    # point. "Left" is the negative of the canonical direction of the line.
    # "Right" is positive.
    left_dist = float("-inf")
    right_dist = float("inf")
    M = 1000 # A sufficiently large number
    slack_var = 0.00
    for prev_line in other_lines:
        num = dot(prev_line.direction, line.point - prev_line.point)
        den = det((line.direction, prev_line.direction))
        
        """Comment this while loop to remove relaxation"""
        
        while num < 0:
            #print("num: ", num)
            slack_var += 0.0001
            num = dot(prev_line.direction, line.point - prev_line.point) + M * slack_var**2
        
        # Check for zero denominator, since ZeroDivisionError (or rather
        # FloatingPointError) won't necessarily be raised if using numpy.
        if den == 0:
            # The half-planes are parallel.
            if num < 0:
                # The intersection of the half-planes is empty; there is no
                # solution.
                '''
                TODO implement Relaxed ORCA here.
                '''
                raise InfeasibleError
            else:
                # The *half-planes* intersect, but their lines don't cross, so
                # ignore.
                continue

        # Signed offset of the point of intersection, relative to the line's
        # anchor point, in units of the line's direction.
        offset = num / den
        if den > 0:
            # Point of intersection is to the right.
            right_dist = min((right_dist, offset))
        else:
            # Point of intersection is to the left.
            left_dist = max((left_dist, offset))

        if left_dist > right_dist:
            # The interval is inconsistent, so the feasible region is empty.
            raise InfeasibleError
    return left_dist, right_dist

def perp(a):
    return array((a[1], -a[0]))

def norm_sq(x):
    return dot(x, x)

def norm(x):
    return sqrt(norm_sq(x))

def normalized(x):
    l = norm_sq(x)
    assert l > 0, (x, l)
    return x / sqrt(l)
