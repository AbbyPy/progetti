"""
    Giorgio Abbadessa
    24 / 05 / 2020
"""

from math import sqrt


def check_degree(vect0, vect1):
    if vect0.degree == vect1.degree: return True
    else: return False

class NotSameDegreeError(TypeError):
    pass

class Vector:

    def __init__(self, comp):
        """ pass the components of a vector in a list """
        self.comp = [float(i) for i in comp]
        self.degree = len(self.comp)

    def __repr__(self):
        return "Vector({})".format(self.comp)

    def __str__(self):
        return "{}".format(self.comp)

    def __add__(self, value):
        """ return self + value """
        if isinstance(value, Vector):
            if check_degree(self, value):
                sum_comp = [self.comp[i]+value.comp[i] for i in range(self.degree)]
                return Vector(sum_comp)
            else:
                raise NotSameDegreeError(value)
        else:
            raise TypeError(value, "must be a vector")

    def __neg__(self):
        """ return -self """
        neg_comp = [-i for i in self.comp]
        return Vector(neg_comp)

    def __sub__(self, value):
        """ return self - value """
        return self + (-value)

    def __abs__(self):
        """return the magnitude of the vector abs(v)"""
        value = 0
        for i in self.comp: 
            value += i**2
        return sqrt(value)

    def __mul__(self, value):
        """ return vector * pure number """
        if type(fact) == float or type(fact) == int:
            mul_comp = [fact*i for i in self.comp]
            return Vector(mul_comp)
        else:
            raise TypeError(value, "must be a pure number (int or flot)")

    def scal_mul(self, value):
        """ return self x value """
        if isinstance(value, Vector):
            if check_degree:
                scal_mul_comp = [self.comp[i]*value.comp[i] for i in range(self.degree)]
                return Vector(scal_mul_comp)
            else:
                raise NotSameDegreeError(value)
        else:
            raise TypeError(value, "must be a vector")

    def vect_mul(self, value):
        pass

    def __truediv__(self, value):
        """ return vector / pure numer """
        return self * (1/value)

    def __eq__(self, value):
        """ return self == value """
        if isinstance(value, Vector):
            if check_degree(self, value):
                if self.comp == value.comp: return True
                else: return False
            else:
                raise NotSameDegreeError(value)
        else:
            raise TypeError(value, "must be a vector")


    def __ne__(self, value):
        """ return self != value """
        return not(self == value)

    def __lt__(self, value):
        """ return self < value """
        if isinstance(value, Vector):
            if check_degree(self, value):
                if abs(self) < abs(value): return True
                else: return False
            else:
                raise NotSameDegreeError(value)
        else: 
            raise TypeError(value, "must be a vector")

    def __gt__(self, value):
        """ return self > value """
        if isinstance(value, Vector):
            if check_degree(self, value):
                if abs(self) > abs(value): return True
                else: return False
            else:
                raise NotSameDegreeError(value)
        else: 
            raise TypeError(value, "must be a vector")

    def __le__(self, value):
        """ return self <= value """
        if isinstance(value, Vector):
            if check_degree(self, value):
                if abs(self) <= abs(value): return True
                else: return False
            else:
                raise NotSameDegreeError(value)
        else: 
            raise TypeError(value, "must be a vector")

    def __ge__(self, value):
        """ return self >= value """
        if isinstance(value, Vector):
            if check_degree(self, value):
                if abs(self) >= abs(value): return True
                else: return False
            else:
                raise NotSameDegreeError(value)
        else: 
            raise TypeError(value, "must be a vector")

# MIGLIORAMENTI DA APPORTARE
# aggiungere in cima a tutti i metodi magic un metodo che controllo se self e un 
# altro vettore value passato hanno lo stesso grado e implementarlo in tutte le funzioni
# poichè con questo modulo è possile fare operazioni solo fra vettori aventi lo stesso
# grado, ossia aventi lo stesso numero di componenti / dimensioni
