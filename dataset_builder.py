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

        meta_data[str(i)] = boundingbox

    '''points.toJSON() for points in boundingbox.points'''
    json_data = {f'{key}.{sample_settings["extension"]}': boundingbox.toJSON() for key, boundingbox in meta_data.items()}
    jsonfile = open(dataset_directory/'meta_data.json', 'w')
    json.dump(json_data, jsonfile, indent=4)
    jsonfile.close()


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
            

generate_dataset()