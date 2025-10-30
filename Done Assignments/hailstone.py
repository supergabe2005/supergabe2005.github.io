#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/22/25
#Description: This program takes a positive integer as the initial number of a
#             hailstone sequence and returns how many steps it takes to reach 1

#define hailstone function
def hailstone(n):
    """
    Return the number of steps it takes to reach 1 in a hailstone sequence.
    Hailstone Sequence:
    starting with a positive integer, if the number is even, divide by 2.
    if the number is odd, multiply by 3 and add 1. Repeat until reaching 1.
    -This function counts how many steps it takes to reach 1.
    argument:
    n: A positive integer representing the starting number of the hailstone sequence.

    returns:
    the number of steps it takes to reach 1. If n is already 1, returns 0.

    example:
    hailstone(3): returns 7 (sequence: 3, 10, 5, 16, 8, 4, 2, 1)
    """
    #initialize step counter
    steps = 0

    #continue looping until n reaches 1
    while n != 1:
        #check if n is even: modulo %
        if n % 2 == 0: #if even
            #divide n by 2
            n = n / 2
        else: #if odd
            #multiply n by 3 and add 1
            n = n * 3 + 1

        #increment the step counter by 1
        steps = steps + 1

    #return total number of steps taken to reach 1
    return steps

