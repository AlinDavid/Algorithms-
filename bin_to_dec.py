'''
Write a program that converts a binary (base 2) number to decimal (base 10). Your
program should begin by reading the binary number from the user as a string. Then
it should compute the equivalent decimal number by processing each digit in the
binary number. Finally, your program should display the equivalent decimal number
with an appropriate message.
'''


def bin_dec(given_number):

    given_number = str(given_number)
    final_number = 0

    for i in given_number:
        final_number = final_number * 2 + int(i)

    return final_number
