class PointVector:
    def __init__(self, coord_x=0, coord_y=0):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def set_coord(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_coord(self):
        self.coord_x = self.x2 - self.x1
        self.coord_y = self.y2 - self.y1

    def __str__(self):
        return f"x coord: {self.coord_x}, y coord: {self.coord_y}"

point = PointVector()
point.set_coord(3, 5, 8, 9)
point.get_coord()
print(point)
