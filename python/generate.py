from generate_lib.import_lib import *

# generates segments of a snowflake
def generate(layers):
    # randomize weather
        conditions = weather(layers)
    # starting element
        segments = starting_element(conditions)
    # generate elements
        for i in range(1,layers):
            segments = generate_element(segments, i, conditions)
    # remove temporary
        for i in range(len(segments)):
            segments[i] = [segment for segment in segments[i] if segment.temporary==0]
    # rotate randomly
        for i in range(len(segments)):
            seed(sum(sum(conditions[:],[])))
            angle = randint(0,360)
            segments[i] = [rotate(segment,angle) for segment in segments[i]]
        return segments