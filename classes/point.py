import json

class Point:

    coordinates = []

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def distanceToOrigin(self):
        # Which distance ? L1/L2-Norm ?
        pass

    def toJSON(self):
        return json.dumps(self.coordinates)