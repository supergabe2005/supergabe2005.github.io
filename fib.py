#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/21/25
#Description: This program will find all fibonacci numbers
#             and return the number listed at position n(input)

#define fibonacci function
def fib(n):
    """
    Return the number at position n in the Fibonacci sequence.
    argument:
    n: A positive integer representing the position in the Fibonacci sequence.

    returns:
    The Fibonacci number at position n.

    example:
    fib(10) returns 55
    """
    #specific case error
    if n == 1 or n == 2:
        return 1
    #initialize previous number and current number
    prev = 1
    current = 1
    #Loops through, adds, and shifts previous number to current
    #and current forward to the next number in the sequence
    for i in range(3, n + 1):
        next_num = prev + current
        prev = current
        current = next_num
    #returns the fibonacci number at position n
    return current