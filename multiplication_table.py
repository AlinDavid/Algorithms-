'''

In this exercise you will create a program that displays a multiplication table that
shows the products of all combinations of integers from 1 times 1 up to and including
10 times 10. Your multiplication table should include a row of labels across the top
of it containing the numbers 1 through 10. It should also include labels down the left
side consisting of the numbers 1 through 10. The expected output from the program
is shown below:

      1    2    3    4    5    6    7    8    9   10
 5    5   10   15   20   25   30   35   40   45   50
 6    6   12   18   24   30   36   42   48   54   60
 7    7   14   21   28   35   42   49   56   63   70
 8    8   16   24   32   40   48   56   64   72   80
 9    9   18   27   36   45   54   63   72   81   90
10   10   20   30   40   50   60   70   80   90  100

'''


def multiplication_table(mn, mx):

    print("  ", end="")

    for i in range(1, mx + 1):
        print("{:>5d}".format(i), end="")
    print()

    for i in range(mn, mx + 1):

        print("{:>2d}".format(i), end="")

        for j in range(1, 11):
            print("{:>5d}".format(i * j), end="")
        print()

    print()

    return "The multiplication table of numbers from range({0},{1})".format(mn, mx)
