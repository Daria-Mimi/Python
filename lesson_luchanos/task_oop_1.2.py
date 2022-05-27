# 1.2
class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self._coord_x = coord_x
        self._coord_y = coord_y

    def set_coord(self, x, y):
        self._coord_x = x
        self._coord_y = y

    def get_coord(self):
        return self._coord_x, self._coord_y

    def __str__(self):
        return f"x coord: {self._coord_x}, y coord: {self._coord_y}"


class DPoint(Point):
    def __init__(self, coord_x=0, coord_y=0, coord_z=0):
        super().__init__(coord_x, coord_y)
        self._coord_z = coord_z

    def set_coord(self, coord_x=0, coord_y=0, coord_z=0):
        super().set_coord(coord_x, coord_y)
        self._coord_z = coord_z

    def get_coord(self):
        return super().get_coord(), self._coord_z

    def __str__(self):
        return f"{super().__str__()}, z coord: {self._coord_z}"


dpoint = DPoint()
dpoint.set_coord(3, 5, 8)
dpoint.get_coord()
print(dpoint)
