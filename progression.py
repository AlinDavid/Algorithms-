'''
Develop a hierarchy of classes for iterating numeric progressions. A numeric progression 
is a sequence of numbers, where each number depends on one or more of the previous numbers. 
For example, an arithmetic progression determines the next number by adding a fixed constant
to the previous value, and a geometric progression determines the next number
by multiplying the previous value by a fixed constant. In general, a progression
requires a first value, and a way of identifying a new value based on one or more
previous values.
'''


class Progression:

    def __init__(self, start=0):
        self._current = start

    def advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self.advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(" ".join(str(next(self)) for _ in range(n)))


class ArithmeticProgression(Progression):

    def __init__(self, increment=1, start=0):
        self._increment = increment
        super().__init__(start)

    def advance(self):
        self._current += self._increment


class GeometricProgression(Progression):

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    def advance(self):
        self._prev, self._current = self._current, self._prev + self._current
