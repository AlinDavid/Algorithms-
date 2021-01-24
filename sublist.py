'''
A sublist is a list that makes up part of a larger list. A sublist may be a list containing
a single element, multiple elements, or even no elements at all. For example, [1],
[2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3] is also a
sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because
the elements 2 and 4 are not adjacent in the longer list. The empty list is a sublist of
any list. As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of itself,
meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].

In this exercise you will create a function, isSublist, that determines whether
or not one list is a sublist of another. Your function should take two lists, larger
and smaller, as its only parameters. It should return True if and only if smaller
is a sublist of larger. Write a main program that demonstrates your function.
'''


def is_sub_list(smaller, larger):

    if len(smaller) > len(larger):
        raise ValueError("The smaller list needs to be shorter than the larger one")

    if not smaller:
        return "This list a sublist of the larger list"

    smaller_1 = []
    index = larger.index(smaller[0])

    for i in range(len(smaller)):
        smaller_1.append(larger[index + i])

    return smaller_1 == smaller
