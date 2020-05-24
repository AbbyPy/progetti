# GIORGIO ABBADESSA 24/5/20
from math import sqrt


class IsntVectorError(TypeError):
    pass

class NotSameDegreeError(TypeError):
    pass

class Vector:

    def __init__(self, comp):
        """ pass the components of a vector in a list """
        self.comp = [float(i) for i in comp]
        self.degree = len(self.comp)

    def __repr__(self):
        """ return repr(self) """
        return "Vector({})".format(self.comp)

    def __str__(self):
        """ return str(self) """
        return "{}".format(self.comp)

    def check(self, value):
        """ return True if value is a vector with same number of 
        components else raise some errors"""    
        if isinstance(value, Vector):
            if self.degree == value.degree: return True
            else: raise NotSameDegreeError(value)
        else: raise IsntVectorError(value)

    def __add__(self, value):
        """ return self + value """
        if self.check(value):
            sum_comp = [self.comp[i]+value.comp[i] for i in range(self.degree)]
            return Vector([sum_comp])

    def __neg__(self):
        """ return -self """
        neg_comp = [-i for i in self.comp]
        return Vector(neg_comp)

    def __sub__(self, value):
        """ return self - value """
        return self + (-vector)

    def __abs__(self):
        """ return |self| (magnitude/module of a vector """
        k = 0
        for i in self.comp: k += i**2
        return sqrt(k)

    def __mul__(self, value):
        """ return vector * pure number """
        if type(value) == float or type(value) == int:
            mul_comp = [value*i for i in self.comp]
            return Vector(mul_comp)
        else: raise TypeError(value, "must be a number")

    def scal_mul(self, value):
        """ return self x value """
        if self.check(value):
            scal_mul_comp = [self.comp[i]*value.comp[i] for i in range(self.degree)]
            return Vector(scal_mul_comp)

    def vect_mul(self, value):
        """ return self · value """
        # not yet implemented, coming sonn
        pass

    def __truediv__(selfm value):
        """ return self / value """
        return self * (1 / value)

    def __eq__(self, value):
        """ return self == value """
        if self.check(value):
            if self.comp == value.comp: return True
            else: return False

    def __ne__(self, value):
        """ return self != value """
        return not(self == value)

    def __lt__(self, value):
        """ return self < value """
        if self.check(value):
            if abs(self) < abs(value): return True
            else: return False

    def __gt__(self, value):
        """ return self > value """
        if self.check(value):
            if abs(self) > abs(value): return True
            else: return False

    def __le__(self, value):
        """ return self <= value """
        if self.check(value):
            if abs(self) <= abs(value): return True
            else: return False

    def __ge__(self, value):
        """ return self >= value """
        if self.check(value):
            if abs(self) >= abs(value): return True
            else: return False
