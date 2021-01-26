'''
Write a Python program that inputs a polynomial in standard algebraic
notation and outputs the first derivative of that polynomial.

Also, i've used the sympy library and added a new method that
result the integral of the current function
'''


from sympy import Symbol, integrate, diff


class Function:

    def __init__(self, func):
        self.func = func

    def derivate(self):

        x = Symbol("x")
        self.func = diff(self.func, x)

        return self.func

    def integrate(self):

        x = Symbol("x")
        self.func = integrate(self.func, x)

        return self.func

    def __repr__(self):
        return "function is {}".format(self.func)
