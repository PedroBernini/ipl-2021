# Programa para representar triângulos no plano.

import math

def isClose(a, b, rel_tol=1e-06, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)

class Triangle():
    def __init__(self, pointA, pointB, pointC):
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
    
    def side_lengths(self):
        return (self.pointA.euclidean_distance(self.pointB),
                self.pointB.euclidean_distance(self.pointC), 
                self.pointC.euclidean_distance(self.pointA))

    def angles(self):
        ab = self.pointA.angle_between(self.pointB)
        ac = self.pointA.angle_between(self.pointC)
        cb = self.pointC.angle_between(self.pointB)
        return [abs(ab - cb), abs(ac - ab), math.pi - (abs(ab - cb) + abs(ac - ab))]

    def side_classification(self):
        sides = self.side_lengths()
        equals = list(set([isClose(sides[i], sides[j]) for i in range(0, len(sides)) for j in range(i + 1, len(sides))]))
        return 'isosceles' if len(equals) != 1 else 'scalene' if equals[0] == False else 'equilateral'

    def angle_classification(self):
        angles = self.angles()
        if self.is_right():
            return 'right'
        if isClose(angles[0], math.pi / 3) and isClose(angles[1], math.pi / 3) and isClose(angles[2], math.pi / 3):
            return 'equiangular'
        if angles[0] < (math.pi / 2) and angles[1] < (math.pi / 2) and angles[2] < (math.pi / 2):
            return 'acute'
        if angles[0] > (math.pi / 2) or angles[1] > (math.pi / 2) or angles[2] > (math.pi / 2):
            return 'obtuse'

    def is_right(self):
        for angle in self.angles():
            if angle == (math.pi) / 2:
                return True
        return False

    def area(self):
        sides = self.side_lengths()
        semi_perimeter = self.perimeter() / 2
        return (semi_perimeter 
        * (semi_perimeter - sides[0]) 
        * (semi_perimeter - sides[1]) 
        * (semi_perimeter - sides[2])) ** 0.5

    def perimeter(self):
        return sum(self.side_lengths())