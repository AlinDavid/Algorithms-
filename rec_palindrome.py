'''
Write a main program that reads a string from the user. Use your recursive function
to determine whether or not the string is a palindrome. Then display an appropriate
message for the user.
'''


def rec_palindrome(given_string, low, high):

    if low == high:
        return True

    if given_string[low] != given_string[high]:
        return False

    if low < high + 1:
        return rec_palindrome(given_string, low + 1, high - 1)
        
