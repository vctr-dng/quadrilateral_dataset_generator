import json

from typing import List

class Point:

    coordinates = []

    def __init__(self, coordinates:List):
        self.coordinates = coordinates

    def distanceToOrigin(self):
        # Which distance ? L1/L2-Norm ?
        pass

    def toJSON(self):
        return self.coordinates