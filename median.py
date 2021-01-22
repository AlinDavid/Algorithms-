'''
Write a function that takes three numbers as parameters, and returns the median value
of those parameters as its result. Include a main program that reads three values from
the user and displays their median.
'''


# Method *1

def median(a, b, c):

    if a < b and a > c or a > b and c > a:
        return a

    if b < a and b > c or b > a and c > b:
        return b

    if c < a and b < c or c > a and b > c:
        return c
        
        
# Method *2 

def alternative_median(a, b, c):

    return a + b + c - min(a, b, c) - max(a, b, c)
