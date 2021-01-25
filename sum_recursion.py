'''
Write a program that reads values from the user until a blank line is entered. Display
the total of all of the values entered by the user (or 0.0 if the first value entered is
a blank line). Complete this task using recursion. Your program may not use any
loops.
'''


def write():

    user_input = input("Write a value (blank to quit) :")

    if not user_input:
        return 0
    else:
        return int(user_input) + write()
   
