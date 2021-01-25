'''
A Bingo card consists of 5 columns of 5 numbers. The columns are labeled with the
letters B, I, N, G and O. There are 15 numbers that can appear under each letter. In
particular, the numbers that can appear under the B range from 1 to 15, the numbers
that can appear under the I range from 16 to 30, the numbers that can appear under
the N range from 31 to 45, and so on.

Write a function that creates a random Bingo card and stores it in a dictionary. The
keys will be the letters B, I, N, G and O. The values will be the lists of five numbers
that appear under each letter. Write a second function that displays the Bingo card
with the columns labeled appropriately. Use these functions to write a program that
displays a random Bingo card. Ensure that the main program only runs when the file
containing your solution has not been imported into another program
'''



from random import randrange


def create_card():

    NUMS_PER_LETTER = 15
    card = dict()
    low = 1
    up = 1 + NUMS_PER_LETTER

    for letter in ["B", "I", "N", "G", "O"]:
        card[letter] = []

        while len(card[letter]) != 2:
            next_num = randrange(low, up)

            if next_num not in card:
                card[letter].append(next_num)

        low += NUMS_PER_LETTER
        up += NUMS_PER_LETTER

    return card


def display_card(card):

    display_list = []

    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            display_list.append(card[letter])

    return display_list
