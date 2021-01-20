'''
The greatest common divisor of two positive integers, n and m, is the largest number,
d, which divides evenly into both n and m.
Write a program that reads two positive integers from the user and uses this algorithm
to determine and report their greatest common divisor.
'''


def biggest_divisor(first_number, second_number):

    big_div = min(first_number, second_number)

    while big_div:

        if first_number % big_div == 0 and second_number % big_div == 0:
            return big_div
        big_div -= 1
        
