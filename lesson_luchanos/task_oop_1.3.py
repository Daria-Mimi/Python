class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.coord_x = coord_x
        self.coord_y = coord_y

    # def set_coord(self, x, y):
    #     self.coord_x = x
    #     self.coord_y = y
    #
    # def get_coord(self):
    #     return self.coord_x, self.coord_y
    #
    # def __str__(self):
    #     return f"x coord: {self.coord_x}, y coord: {self.coord_y}"


class Vector:
    def __init__(self, vec_a, vec_b):
        if type(vec_a) == Point and type(vec_b) == Point:
            self.coord_x = vec_b.coord_x - vec_a.coord_x
            self.coord_y = vec_b.coord_y - vec_a.coord_y
        else:
            self.coord_x = vec_a
            self.coord_y = vec_b

    def __add__(self, other):
        coord_x_new = self.coord_x + other.coord_x
        coord_y_new = self.coord_y + other.coord_y
        return Vector(coord_x_new, coord_y_new)

    def __sub__(self, other):
        coord_x_new = self.coord_x - other.coord_x
        coord_y_new = self.coord_y - other.coord_y
        return Vector(coord_x_new, coord_y_new)

    def __mul__(self, num):
        coord_x_new = self.coord_x * num
        coord_y_new = self.coord_y * num
        return Vector(coord_x_new, coord_y_new)

    def __truediv__(self, num):
        coord_x_new = self.coord_x / num
        coord_y_new = self.coord_y / num
        return Vector(coord_x_new, coord_y_new)

    def get_coord(self):
        return self.coord_x, self.coord_y

    def __str__(self):
        return f"coord a : {self.coord_x}, coord b : {self.coord_y}"

p1 = Point(3, 5)
p2 = Point(8, 9)
vect = Vector(p1, p2)
print(vect)

# сложение
vec_1 = Vector(3, 4)
vec_2 = Vector(5, 6)
vec_new = vec_1 + vec_2
print(vec_new)

# вычитание
vec_1 = Vector(3, 4)
vec_2 = Vector(5, 6)
vec_new = vec_1 + vec_2
print(vec_new)

# умножение
vec_1 = Vector(3, 4)
vec_new = vec_1 * 2
print(vec_new)

# деление
vec_1 = Vector(4, 8)
vec_new = vec_1 / 2
print(vec_new)