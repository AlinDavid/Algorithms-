'''
This exercise examines the process of identifying the maximum value in a collection
of integers. Each of the integers will be randomly selected from the numbers between
1 and 100. The collection of integers may contain duplicate values, and some of the
integers between 1 and 100 may not be present.
Take a moment and think about how you would handle this problem on paper.
Many people would check each integer in sequence and ask themself if the number
that they are currently considering is larger than the largest number that they have seen
previously. If it is, then they forget the previous maximum number and remember
the current number as the new maximum number. This is a reasonable approach,
and will result in the correct answer when the process is performed carefully. If you
were performing this task, how many times would you expect to need to update the
maximum value and remember a new number?
Exercise 79: Maximum Integer 37
While we can answer the question posed at the end of the previous paragraph using
probability theory, we are going to explore it by simulating the situation. Create a
program that begins by selecting a random integer between 1 and 100. Save this
integer as the maximum number encountered so far. After the initial integer has been
selected, generate 99 additional random integers between 1 and 100. Check each
integer as it is generated to see if it is larger than the maximum number encountered
so far. If it is then your program should update the maximum number encountered
and count the fact that you performed an update.

Execution model:

Current maximum is 21

52 <== Update
40
80 <== Update
10
26
...
36

The maximum value found was 99
The maximum was updated 7 times
'''

import random


def highest_integer():

    current_maximum = random.randint(1, 100)
    print("Current maximum is {}\n".format(current_maximum))
    number_list = []
    updates = 0

    for i in range(1, 101):

        number_list.append(random.randint(1, 100))
        print(number_list[i - 1], end="")

        if number_list[i - 1] > current_maximum:
            
            current_maximum = number_list[i - 1]
            print(" <== Update")
            updates += 1
            continue
            
        print()
    print("\nThe maximum value found was {}".format(current_maximum))
    print("The maximum was updated {} times".format(updates))
    
    return None
