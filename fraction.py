class Fraction:

    def __init__(self, top, bottom):
        if type(top) == int and type(bottom) == int:
            self.num = top
            self.den = bottom
        else:
            raise TypeError("Wrong input type: {} and {}".format(type(top), type(bottom)))