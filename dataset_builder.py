from typing import Iterable, Tuple
from pathlib import Path

import os
import random
import json
import csv

from classes.sample import Sample
from classes.settings_loader import Settings_Loader
from classes.boundingbox import BoundingBox
from classes.point import Point
from classes.dataset import RectangleDataset
from classes.random_rectangle import Random_Rectangle

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

        boundingbox = BoundingBox(Random_Rectangle.generate(sample_settings['dim'], sample_settings['polygon']['dim']))

        sample = Sample(boundingbox, sample_settings)
        sample.draw()
        sample.save_image(dataset_directory, i)

        meta_data[str(i)] = boundingbox

    # JSON metadata
    json_data = {f'{key}.{sample_settings["extension"]}': boundingbox.toJSON() for key, boundingbox in meta_data.items()}
    jsonfile = open(dataset_directory/'meta_data.json', 'w')
    json.dump(json_data, jsonfile, indent=4)
    jsonfile.close()

    # CSV metadata
    csv_data = []
    for key, boundingbox in meta_data.items():
        unpacked_coordinates = []
        for point in boundingbox.points:
            unpacked_coordinates += point.coordinates
        
        row = [f'{key}.{sample_settings["extension"]}'] + unpacked_coordinates

        csv_data.append(row)
    csvfile = open(dataset_directory/'meta_data.csv', 'w')
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerows(csv_data)
    csvfile.close()

    """ rectangle_ds = RectangleDataset(str(dataset_directory/'meta_data.csv'), dataset_settings)
    print(rectangle_ds.__getitem__(0)['label']) """

    

generate_dataset()