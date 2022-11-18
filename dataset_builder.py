## PARAMETERS

from PIL import Image, ImageDraw

from typing import Iterable, Tuple

from pathlib import Path

import os
import random

import conf_setup

dataset_directory = Path("dataset")

num_sample = 100
sample_dim = (256, 256)
bg_color = 'black'
rectangle_color = 'white'
rectangle_dim = (75,30)

def create_sample(endpoints:Iterable[Tuple[int, int]]):
    img = Image.new("RGB", sample_dim, bg_color)
    drawer = ImageDraw.Draw(img)
    drawer.rectangle(endpoints, fill=rectangle_color)

    return img, drawer

def random_linked_integer(axis:int):
    integer1 = random.randint(0, sample_dim[axis]-1)
    integer2 = integer1

    if integer2 + rectangle_dim[axis] > sample_dim[axis]:
        integer2 -= rectangle_dim[axis]
    elif integer2 - rectangle_dim[axis] < 0:
        integer2 += rectangle_dim[axis]
    else:
        rand_operator = random.randint(0, 1)
        if rand_operator == 0:
            integer2 -= rectangle_dim[axis]
        else:
            integer2 += rectangle_dim[axis]
    
    return integer1, integer2

def generate_dataset():
    for i in range(num_sample):
        randx1, randx2 = random_linked_integer(0)
        randy1, randy2 = random_linked_integer(1)
        endpoints = [(randx1, randy1), (randx2, randy2)]

        img, drw = create_sample(endpoints)
        img.save(dataset_directory/f'{i}.png', 'PNG')

generate_dataset()