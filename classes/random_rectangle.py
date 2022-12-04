import random

from classes.point import Point

class Random_Rectangle:
    
    @staticmethod
    def random_dimension(sample_dimension):
        pass

    @staticmethod
    def random_linked_integer(axis:int, sample_dimension, rectangle_dimension):
        int0 = random.randint(0, sample_dimension[axis]-1)
        int1 = int0

        if int1 + rectangle_dimension[axis] > sample_dimension[axis]:
            int1 -= rectangle_dimension[axis]
        elif int1 - rectangle_dimension[axis] < 0:
            int1 += rectangle_dimension[axis]
        else:
            rand_operator = random.randint(0, 1)
            if rand_operator == 0:
                int1 -= rectangle_dimension[axis]
            else:
                int1 += rectangle_dimension[axis]
        
        return [int0, int1]
    
    @staticmethod
    def random_location(sample_dimension, rectangle_dimension):

        random_axis = []

        for i in range(len(rectangle_dimension)):
            random_axis.append(Random_Rectangle.random_linked_integer(i, sample_dimension, rectangle_dimension))

        return random_axis

    @staticmethod
    def generate(sample_dimension, rectangle_dimension):
        
        #TODO: random rectangle size
        if not rectangle_dimension:
            pass

        random_axis = Random_Rectangle.random_location(sample_dimension, rectangle_dimension)

        points = [
            Point([random_axis[0][0], random_axis[1][0]]),
            Point([random_axis[0][1], random_axis[1][0]]),
            Point([random_axis[0][1], random_axis[1][1]]),
            Point([random_axis[0][0], random_axis[1][1]])
        ]

        return points