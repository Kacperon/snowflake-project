from generate_lib.import_lib import *

# generates segments of a snowflake
def generate(layers):
    # randomize weather
        conditions = weather(layers)
    # starting element
        segments = starting_element(conditions)
    # generate elements
        for i in range(layers):
            segments = generate_element(segments,i,conditions)
    # remove temporary

        return segments