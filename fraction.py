def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:

    def __init__(self, top, bottom):
        if type(top) == int and type(bottom) == int:
            if bottom < 0:
                raise ValueError("Negative fraction should have negative numerator not denominator")
            elif top == 0 or bottom == 0:
                raise ValueError("Denominator and numerator should not be equal to zero")
            else:
                self.num = top
                self.den = bottom
        else:
            raise TypeError("Wrong input type: {} and {}".format(type(top), type(bottom)))

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        if other == 0:
            return self
        else:
            new_num = self.num*other.den + other.num*self.den
            new_den = self.den*other.den
            reduction = gcd(new_num, new_den)
            return Fraction(new_num//reduction, new_den//reduction)

    def __eq__(self, other):
        if other == 0:
            return False
        else:
            return self.num == other.num and self.den == other.den

    def __sub__(self, other):
        if other == 0:
            return self
        new_num = self.num*other.den - other.num*self.den
        new_den = self.den*other.den
        if new_num == 0 or new_den == 0:
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