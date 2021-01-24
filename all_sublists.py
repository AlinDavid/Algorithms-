'''
Write a function that returns a listcontaining every possible sublist of a list. For example, 
the sublists of [1, 2, 3] are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that 
your function will always return a list containing at least the empty list because the empty list
is a sublist of every list. Include a main program that demonstrate your function by
displaying all of the sublists of several different lists.
'''


def all_sublist(biggest_guy):

    smaller_guy = []

    for lentgh in range(1, len(biggest_guy) + 1):
        for i in range(len(biggest_guy) - lentgh + 1):
            smaller_guy.append(biggest_guy[i:i + lentgh])

    return smaller_guy
    
