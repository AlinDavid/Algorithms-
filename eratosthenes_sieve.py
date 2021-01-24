'''
The Sieve of Eratosthenes is a technique that was developed more than 2,000 years
ago to easily find all of the prime numbers between 2 and some limit, say 100.

The key to this algorithm is that it is relatively easy to cross out every nth number
on a piece of paper. This is also an easy task for a computer—a for loop can simulate
this behavior when a third parameter is provided to the range function. When a
number is crossed out, we know that it is no longer prime, but it still occupies space on
the piece of paper, and must still be considered when computing later prime numbers.

As a result, you should not simulate crossing out a number by removing it from the
list. Instead, you should simulate crossing out a number by replacing it with 0. Then,
once the algorithm completes, all of the non-zero values in the list are prime.
Create a Python program that uses this algorithm to display all of the prime
numbers between 2 and a limit entered by the user. If you implement the algorithm
correctly you should be able to display all of the prime numbers less than 1,000,000
in a few seconds.
'''

def erastothene(limit):

    nums = [i for i in range(limit + 1)]
    nums[1] = 0
    p = 2

    while p < limit // 2:

        for i in range(p * 2, limit + 1, p):
            nums[i] = 0

        p += 1

        while p < limit and nums[p] == 0:
            p += 1

    return [i for i in nums if i != 0]
