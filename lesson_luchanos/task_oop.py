# 1.1
class Point:
    def coord(self, x, y):
        self.__coord_x = x
        self.__coord_y = y

    def get_coord(self):
        return f"x coord: {self.__coord_x}, y coord: {self.__coord_y}"


point = Point()
point.coord(3, 5)
print(point.get_coord())


