def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:

    def __init__(self, top, bottom):
        if type(top) == int and type(bottom) == int:
            if top == 0 or bottom == 0:
                raise ValueError("Denominator and numerator should not be equal to zero")
            elif top < 0 and bottom < 0:
                reduction = gcd(abs(top), abs(bottom))
                self.num = abs(top)//reduction
                self.den = abs(bottom)//reduction
            elif bottom < 0:
                reduction = gcd(top, abs(bottom))
                self.num = -top//reduction
                self.den = abs(bottom)//reduction
            else:
                reduction = gcd(top, bottom)
                self.num = top//reduction
                self.den = bottom//reduction
        else:
            raise TypeError("Wrong input type: {} and {}".format(type(top), type(bottom)))

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        return "Fraction(%s, %s)" % (self.num, self.den)

    def __add__(self, other):
        if other == 0:
            result = self
        else:
            new_num = self.num*other.den + other.num*self.den
            new_den = self.den*other.den
            if new_num == 0:
                result = 0
            else:
                result = Fraction(new_num, new_den)
        return result

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            raise NotImplementedError("This type of addition is not implemented")

    def __iadd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if other == 0:
            return False
        else:
            return self.num == other.num and self.den == other.den

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if other == 0:
            return self.num < 0
        else:
            return self.num*other.den < other.num*self.den

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if other == 0:
            return self.num > 0
        else:
            return self.num*other.den > other.num*self.den

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __sub__(self, other):
        if other == 0:
            return self
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den
        if new_num == 0:
            return 0
        else:
            reduction = gcd(new_num, new_den)
            return Fraction(new_num//reduction, new_den//reduction)

    def __mul__(self, other):
        if other == 0:
            return 0
        else:
            new_num = self.num*other.num
            new_den = self.den*other.den
            reduction = gcd(new_num, new_den)
            return Fraction(new_num//reduction, new_den//reduction)

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("Can not divide fraction by zero")
        else:
            new_num = self.num*other.den
            new_den = self.den*other.num
            reduction = gcd(new_num, new_den)
            return Fraction(new_num//reduction, new_den//reduction)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den