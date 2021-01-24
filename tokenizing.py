'''
Tokenizing is the process of converting a string into a list of substrings, known as
tokens. In many circumstances, a list of tokens is far easier to work with than the
original string because the original string may have irregular spacing. In some cases
substantial work is also required to determine where one token ends and the next one
begins.

In a mathematical expression, tokens are items such as operators, numbers and
parentheses. Some tokens, such as *, /, ˆ, ( and ) are easy to identify because the
token is a single character, and the character is never part of another token. The + and
- symbols are a little bit more challenging to handle because they might represent
the addition or subtraction operator, or they might be part of a number token.

Write a function that takes a string containing a mathematical expression as its
only parameter and breaks it into a list of tokens. Each token should be a parenthesis,
an operator, or a number with an optional leading + or - (for simplicity we will
only work with integers in this problem). Return the list of tokens as the function’s
result.

You may assume that the string passed to your function always contains a valid
mathematical expression consisting of parentheses, operators and integers. However, 
your function must handle variable amounts of whitespace between these
elements.
'''


def token_list(word):

    tokens = []
    i = 0

    while i < len(word):

        if word[i] == "*" or word[i] == "/" or word[i] == "^" or word[i] == "(" or word[i] == ")":

            tokens.append(word[i])
            i += 1

        elif word[i] == "+" or word[i] == "-":

            if i > 0 and ("0" <= word[i - 1] <= "9" or word[i - 1] == ")"):

                tokens.append(word[i])
                i += 1

            else:

                num = word[i]
                i += 1

                while i < len(word) and "0" <= word[i] <= "9":
                    num = num + word[i]
                    i += 1

                tokens.append(num)

        elif "0" <= word[i] <= "9":

            num = ""

            while i < len(word) and "0" <= word[i] <= "9":
                num = num + word[i]
                i += 1

        else:
            return []

    return tokens
   
