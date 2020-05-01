class Poly:
                    
    def __init__(self, coeff_list):
        
        def remove_zeros():
            back = self.coeff[::-1]
            for i in back:
                if i == 0:
                    self.coeff.pop()
                else:
                    break

        if type(coeff_list) != list:
            raise ValueError("coeff list must be a list")
        else:
            self.coeff = [float(i) for i in coeff_list]
            remove_zeros()

    def __str__(self):
        str_value = ""
        for i in range(len(self.coeff)):
            if self.coeff[i] < 0:
                str_value += f"{self.coeff[i]} * x^{i}  "
            if self.coeff[i] > 0:
                str_value += f"+{self.coeff[i]} * x^{i}  "
        return str_value

    def __repr__(self):
        repr_value = f"Poly({self.coeff})"
        return repr_value

    def __gt__(self, value):
        # return self > value
        if len(self.coeff) > len(value.coeff):
            return True
        else:
            return False

    def __lt__(self, value):
        # return self < value
        if len(self.coeff) < len(value.coeff):
            return True
        else:
            return False
    
    def __eq__(self, value):
        # return self == value
        if self.coeff == value.coeff:
            return True
        else:
            return False
    
    def __add__(self, other):
        sum_coeff = []
        if self < other:
            for i in range(len(self.coeff)):
                sum_coeff.append(self.coeff[i] + other.coeff[i])
            for k in range(i+1, len(other.coeff)):
                sum_coeff.append(other.coeff[k])
            #sum_coeff[i+1:] = [k for k in other.coeff[i+1:]]
        if self > other:
            for i in range(len(other.coeff)):
                sum_coeff.append(self.coeff[i] + other.coeff[i])
            for k in range(i+1, len(self.coeff)):
                sum_coeff.append(self.coeff[k])
            #sum_coeff[i+1:] = [k for k in other.coeff[i+1:])
        if len(self.coeff) == len(other.coeff):
            sum_coeff = [x + y for x, y in zip(self.coeff, other.coeff)]
        return Poly(sum_coeff)

    def __sub__(self, other):
        subtractor_coeff = [-i for i in other.coeff]
        subtractor = Poly(subtractor_coeff)
        return self + subtractor



p1 = Poly([3, 2, 1, 0, 3, 2, 0])
p2 = Poly([0, 5, 3, 1, 0, 0, 1, 0, 2])

print(repr(p1+p2))
print(repr(p1-p2))
