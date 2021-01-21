'''
What’s the minimum number of times you have to flip a coin before you can have
three consecutive flips that result in the same outcome (either all three are heads or
all three are tails)? What’s the maximum number of flips that might be needed? How
many flips are needed on average? In this exercise we will explore these questions
by creating a program that simulates several series of coin flips.
Create a program that uses Python’s random number generator to simulate flipping
a coin several times. The simulated coin should be fair, meaning that the probability
of heads is equal to the probability of tails. Your program should flip simulated
coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
time the outcome is heads, and a T each time the outcome is tails, with all of the
outcomes shown on the same line. Then display the number of flips needed to reach
3 consecutive flips with the same outcome. When your program is run it should
perform the simulation 10 times and report the average number of flips needed.
Sample output is shown below:

T H H T H H H (6 flips)
T T H T T H H T H T H H T H T T T (16 flips)
H T T T (3 flips)
T H T T H T H H T H H T T T (13 flips)
H H T T H H H (6 flips)
T T H T T T (5 flips)
On average, 8.166666666666666 flips were needed
'''

import random


def flips(performs):

    current = 0             # current perform
    cons_flips = 1              # counts to maximum of 3 same flips
    flips_list = [random.choice(["H", "T"])]            # list of flips of the current run
    current_flip = 0            # all the flips of the current run
    total_flips = 0             # all the flips of the performs

    while current < performs:

        while cons_flips < 3:

            current_flip += 1
            flips_list.append(random.choice(["H", "T"]))

            if flips_list[current_flip] == flips_list[current_flip - 1]:
                cons_flips += 1
            else:
                cons_flips = 1

            if cons_flips == 3:
                print(" ".join(flips_list) + " ({} flips)".format(current_flip))
                total_flips += current_flip

        flips_list = [random.choice(["H", "T"])]
        current_flip = 0
        current += 1
        cons_flips = 1

        if current == performs:
            print("On average, {:2} flips were needed".format(total_flips / performs))
            
