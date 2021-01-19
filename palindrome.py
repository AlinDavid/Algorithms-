'''
A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words.Write a program
that reads a string from the user and uses a loop to determines whether or not it is a
palindrome. Display the result, including a meaningful output message.
'''


# Method *1

def palindrome(given_string):

    is_palindrome = True
    length = len(given_string)

    for i in range(0, length // 2):
        if given_string[i] != given_string[length - i - 1]:
            is_palindrome = False

    if is_palindrome:
        return "The given string is a palindrome"
    else:
        return "The given string is not a palindrome"


# Method *2

# def palindrome(given_string):
#
#     if given_string == given_string[::-1]:
#         return ("This string is a palindrome")
