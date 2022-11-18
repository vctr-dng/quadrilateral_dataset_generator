from typing import Iterable, Tuple, Dict

from PIL import Image, ImageDraw

from classes.settings_loader import Settings_Loader

class Sample:
    
    """
    [0]------[1]
     |        |
     |        |
    [4]------[2]
    """

    def __init__(self, endpoints:Iterable[Tuple[int, int]], sample_settings:Dict):

        self.endpoints = [
            endpoints[0],
            (endpoints[1][0], endpoints[0][1]),
            endpoints[1],
            (endpoints[0][0], endpoints[1][1])
        ]

        self.image = Image.new("RGB", sample_settings['dim'], sample_settings['color'])
        self.drawer = ImageDraw.Draw(self.image)
        self.drawer.rectangle(endpoints, fill=sample_settings['rectangle']['color'])

    
    def save_image(self, directory, name):
        self.image.save(directory/f'{name}.png', 'PNG')