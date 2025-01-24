from generate_lib.import_lib import *

# generates segments of a snowflake
def generate(layers):
    segments = []
    # repeat all if failed
    while len(segments) < layers:
    # randomize weather
        conditions = weather(layers)
    # starting element
        segments = starting_element(conditions)
    # generate elements
        for i in range(1,layers):
            segments = generate_element(segments, i, conditions)
    # remove temporary and empty
        for i in range(len(segments)):
            segments[i] = [segment for segment in segments[i] if segment.temporary==0]
        segments = [element for element in segments if element]
    # rotate randomly
        for i in range(len(segments)):
            seed(int("".join([str(x) for x in sum(conditions,[])])))
            angle = randint(0,360)
            segments[i] = [rotate(segment,angle) for segment in segments[i]]
    return segments