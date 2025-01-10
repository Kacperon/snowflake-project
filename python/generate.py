from random import randint
from Segment import *

def generate_example():
    segments = [Segment(0,0,0,1),Segment(0,1,1/2,2),Segment(0,1,-1/2,2)]
    return segments

def weather():
    steps = 5
    conditions = []
    for i in range(steps):
        temperature = randint(1, 5)
        humidity = randint(1,5)
        conditions.append([temperature, humidity])
    return conditions

def generate():
    conditions = weather()

    return segments