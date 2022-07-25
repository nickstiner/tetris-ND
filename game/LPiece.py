from Shape import *
class LPiece(Shape):

    def __init__(self,orientation,drop_speed):
        Shape.__init__(self,drop_speed)
        self.orientation=orientation
        