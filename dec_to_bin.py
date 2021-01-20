'''
Write a program that converts a decimal (base 10) number to binary (base 2). Read the
decimal number from the user as an integer and then use the division algorithm shown
below to perform the conversion. When the algorithm completes, result contains the
binary representation of the number.
'''


def dec_bin(given_number):

    result = ""

    while given_number != 0:

        remainder = given_number % 2
        result = str(remainder) + result
        given_number //= 2

    return result
