from .Segment import *
from .miscellaneous import rotate

# returns starting element based on conditions
def starting_element(conditions):
        temperature, humidity = conditions[0]
        element = []
        def rotate60():
            for i in range(5):
                element.append(rotate(element[-1], 60))
        def rotate30():
            for i in range(11):
                element.append(rotate(element[-1], 30))
    # zwykłe kreski
        if temperature==1 and humidity==1:
            element.append(Segment(0, 0, 0, 1))
            rotate60()
    # gwiazda 12 ramienna
        if temperature==1 and humidity==2:
            element.append(Segment(0, 0, 0, 4))
            rotate60()
            element.append(rotate(Segment(0, 0, 0, 3),30))
            rotate60()
            element.append(Segment(0, 1.5, -0.5176380902050415, 1.9318516525781366, growing=0))
            rotate30()
            element.append(Segment(0, 1.5, 0.5176380902050415, 1.9318516525781366, growing=0))
            rotate30()
    # dwunastokąt
        if temperature==1 and humidity==3:
            element.append(Segment(0, 0, 0, 2, temporary=1))
            rotate60()
            element.append(Segment(0, 2, -1, 1.7320508075688774,growing=0))
            rotate30()
    # hexagon pusty
        if temperature==2 and humidity==1:
            element.append(Segment(0, 0, 0, 1, temporary=1))
            rotate60()
            element.append(Segment(0, 1, -0.8660254037844386, 0.5, growing=0))
            rotate60()
    # hexagon z hexagonem
        if temperature==2 and humidity==2:
            element.append(Segment(0, 1, 0, 2))
            rotate60()
            element.append(Segment(0, 1, -0.8660254037844386, 0.5, growing=0))
            rotate60()
            element.append(Segment(0, 2, -1.7320508075688772, 1, growing=0))
            rotate60()
    # gwiazdka z gwiazdką
        if temperature==2 and humidity==3:
            element.append(Segment(0, 2, 0, 4))
            rotate60()
            element.append(Segment(-1.25, 2.165063509461097, 0, 4, growing=0))
            rotate60()
            element.append(Segment(1.25, 2.165063509461097, 0, 4, growing=0))
            rotate60()
            element.append(Segment(-0.5, 0.8660254037844387, 0, 2, growing=0))
            rotate60()
            element.append(Segment(0.5, 0.8660254037844387, 0, 2, growing=0))
            rotate60()
    # gwiazdka ostra 1
        if temperature==3 and humidity==1:
            element.append(Segment(0, 0, 0, 1))
            rotate60()
            element.append(Segment(0, 1, -1.5, 2.598076211353316, growing=0))
            rotate60()
            element.append(Segment(0, 1, 1.5, 2.598076211353316, growing=0))
            rotate60()
    # gwiazdka ostra 2
        if temperature==3 and humidity==2:
            element.append(Segment(0, 0, 0, 3, temporary=1))
            rotate60()
            element.append(Segment(-0.5, 0.8660254037844387, 0, 3, growing=0))
            rotate60()
            element.append(Segment(0.5, 0.8660254037844387, 0, 3, growing=0))
            rotate60()
    # gwiazdka z hexagonem
        if temperature==3 and humidity==3:
            element.append(Segment(0, 1, 0, 1.5))
            rotate60()
            element.append(Segment(0, 1, -0.8660254037844386, 0.5, growing=0))
            rotate60()
            element.append(Segment(0, 1.5, -1.5, 2.598076211353316, growing=0))
            rotate60()
            element.append(Segment(0, 1.5, 1.5, 2.598076211353316, growing=0))
            rotate60()

        return [element]