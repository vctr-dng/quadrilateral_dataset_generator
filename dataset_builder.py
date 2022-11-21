from typing import Iterable, Tuple
from pathlib import Path

import os
import random
import json

from classes.sample import Sample
from classes.settings_loader import Settings_Loader
from classes.boundingbox import BoundingBox
from classes.point import Point

import conf_setup

S_L = Settings_Loader()
dataset_settings = S_L.settings_content['dataset']
sample_settings = dataset_settings['sample']

dataset_directory = Path("dataset")

def random_linked_integer(axis:int):
    integer1 = random.randint(0, sample_settings['dim'][axis]-1)
    integer2 = integer1

    if integer2 + sample_settings['polygon']['dim'][axis] > sample_settings['dim'][axis]:
        integer2 -= sample_settings['polygon']['dim'][axis]
    elif integer2 - sample_settings['polygon']['dim'][axis] < 0:
        integer2 += sample_settings['polygon']['dim'][axis]
    else:
        rand_operator = random.randint(0, 1)
        if rand_operator == 0:
            integer2 -= sample_settings['polygon']['dim'][axis]
        else:
            integer2 += sample_settings['polygon']['dim'][axis]
    
    return integer1, integer2

def generate_dataset():
    meta_data = {}
    
    for i in range(dataset_settings['num_sample']):
        randx1, randx2 = random_linked_integer(0)
        randy1, randy2 = random_linked_integer(1)

        boundingbox = BoundingBox(
            [
                Point([randx1, randy1]),
                Point([randx2, randy1]),
                Point([randx2, randy2]),
                Point([randx1, randy2])
            ]
        )

        sample = Sample(boundingbox, sample_settings)
        sample.draw()
        sample.save_image(dataset_directory, i)

        meta_data[str(i)] = [points.toJSON() for points in boundingbox.points]

    jsonfile = open(dataset_directory/'meta_data.json', 'w')
    json.dump(meta_data, jsonfile, indent=4)

generate_dataset()