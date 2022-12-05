from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        sides = [a, b, c]
        sides = sorted(sides)

        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]

    def is_valid(self):
        if (self.a+self.b > self.c) and (self.b+self.c > self.a) and (self.c+self.a > self.b):
            return 'Valid'
        else:
            return 'Invalid'

    def Side_Classification(self):
        if self.is_valid() == 'Valid':
            if (self.a == self.b == self.c):
                return 'Equilateral'
            if (self.a == self.b != self.c) or (self.b == self.c != self.a) or (self.c == self.a != self.b):
                return 'Isosceles'
            if (self.a != self.b != self.c):
                return 'Scalene'
        else:
            return 'Invalid'

    def Angle_Classification(self):
        if self.is_valid() == 'Valid':
            if (self.a**2+self.b**2 > self.c**2):
                return 'Acute'
            if (self.a**2+self.b**2 == self.c**2):
                return 'Right'
            if (self.a**2+self.b**2 < self.c**2):
                return 'Obtuse'
        else:
            return 'Invalid'

        print(self.a, self.b, self.c)

    def Area(self):
        if self.is_valid() == 'Valid':
            self.s = (self.a+self.b+self.c)/2
            self.area = sqrt(self.s*(self.s-self.a) *
                             (self.s-self.b)*(self.s-self.c))

            return self.area
        else:
            return 'Invalid'


T = Triangle(4, 3, 2)
print(T.is_valid())
print(T.Side_Classification())
print(T.Area())
print(T.Angle_Classification())
