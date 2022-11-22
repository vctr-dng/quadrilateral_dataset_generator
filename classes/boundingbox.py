class BoundingBox:

    points = []

    def __init__(self, points):
        self.points = points

    def toJSON(self):
        return [point.toJSON() for point in self.points]