from Shape import *
class TPiece(Shape):

    def __init__(self,orientation):
        Shape.__init__(self)
        self.orientation=orientation