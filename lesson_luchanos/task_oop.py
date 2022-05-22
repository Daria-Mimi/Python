# 1.1
class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.__coord_x = coord_x
        self.__coord_y = coord_y

    def coord(self, x, y):
        self.__coord_x = x
        self.__coord_y = y

    def __str__(self):
        return f"x coord: {self.__coord_x}, y coord: {self.__coord_y}"

    def __repr__(self):
        return f"x coord: {self.__coord_x}, y coord: {self.__coord_y}"


point = Point()
point.coord(3, 5)
print(point)
