import matplotlib.pyplot as plt
import numpy as np
import cmath



class GridDeform:

    def __init__(self, func, radius, center, fit):
        """ func - funzione complessa da studiare;
            radius -  raggio dell'intorno in cui si vuole
            osservare la funzione complessa;
            center - numero complesso centro dell'intorno;
            fit - numero intero che determina quanto fitta sara'
            la griglia """
        self.f = func
        self.r = radius
        self.z0 = center
        self.fit = fit
        self.realAxis = np.linspace(self.z0.real - self.r, self.z0.real + self.r, fit)
        self.imagAxis = np.linspace(self.z0.real - self.r, self.z0.real + self.r, fit)

    def vertLines(self):
        u, v = [], []
        for x in self.realAxis:
            xi = []
            eta = []
            for y in self.imagAxis:
                result = self.f(complex(x, y))
                xi.append(result.real)
                eta.append(result.imag)
            u.append(xi)
            v.append(eta)
        return u, v

    def orizLines(self):
        u, v = [], []
        for y in self.imagAxis:
            xi = []
            eta = []
            for x in self.realAxis:
                result = self.f(complex(x, y))
                xi.append(result.real)
                eta.append(result.imag)
            u.append(xi)
            v.append(eta)
        return u, v

    def plot(self):
        u, v = self.vertLines()
        h, k = self.orizLines()
        for i in range(self.fit):
            plt.plot(u[i], v[i], 'b-')
            plt.plot(h[i], k[i], 'r-')
        plt.show()



# esempio
def foo(z):
    return cmath.exp(z**(1.0))

g = GridDeform(foo, .001, 0, 30)
g.plot()


            





