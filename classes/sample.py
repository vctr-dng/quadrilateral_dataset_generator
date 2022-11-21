from typing import Iterable, Tuple, Dict

from PIL import Image, ImageDraw

from classes.settings_loader import Settings_Loader
from classes.boundingbox import BoundingBox

class Sample:
    
    """
    [0]------[1]
     |        |
     |        |
    [4]------[2]
    """

    def __init__(self, boundingbox:BoundingBox, sample_settings:Dict):

        self.boundingbox = boundingbox
        self.settings = sample_settings

        self.image = Image.new("RGB", sample_settings['dim'], sample_settings['color'])
        self.drawer = ImageDraw.Draw(self.image)
    
    def draw(self):
        list_points = [tuple(point.coordinates) for point in self.boundingbox.points]
        self.drawer.polygon(list_points, fill=self.settings['polygon']['color'])

    
    def save_image(self, directory, name):
        self.image.save(directory/f'{name}.png', 'PNG')