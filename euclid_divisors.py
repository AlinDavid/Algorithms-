'''
Euclid was a Greek mathematician who lived approximately 2,300 years ago. His
algorithm for computing the greatest common divisor of two positive integers, a and
b, is both efficient and recursive.

Write a program that implements Euclid’s algorithm and uses it to determine the
greatest common divisor of two integers entered by the user.
'''

def euclid_divisor(first_number, second_number):

    if second_number == 0:
        return first_number
    else:
        divisor = first_number % second_number
        return euclid(second_number, divisor)
   
   
