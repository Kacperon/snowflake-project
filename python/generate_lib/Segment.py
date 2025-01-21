class Segment:
    def __init__(self,x1,y1,x2,y2,growing=1,temporary=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.growing = growing
        self.temporary = temporary