'''
Write a program that reads an integer from the user. If the value entered by the
user is less than 2 then your program should display an appropriate error message.
Otherwise your program should display the prime numbers that can be multiplied
together to compute n, with one factor appearing on each line. For example:

The prime factors of 72 are:
2
2
2
3
3
'''

# Method *1

def prime_factors(given_number):

    factor = 2
    prime_list = []

    print("The prime factors of {} are:".format(given_number))

    while factor <= given_number:
        if given_number % factor == 0:
            prime_list.append(factor)
            given_number = given_number / factor
        else:
            factor += 1

    return "\n".join(str(i) for i in prime_list)

# Method *2 is posted on my other repository, Exercism
