#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 11/12/25
#Description: this function returns the product of two positive integers using only addition using recursion

def multiply(a, b):
    """
    returns the product of two positive integers using only addition.

    this function uses recursion to multiply two numbers by repeatedly
    adding one number to itself. The function breaks down the multiplication
    into a series of additions with a recursive base case.

    logic: a * b = a + (a * (b - 1))
    base case: a * 1 = a

    args:
    a (int): First positive integer
    b (int): Second positive integer

    returns:
    int: The product of a and b
    """

    #base case: any number times 1 equals that number
    if b == 1:
        return a

    #recursive case: a * b = a + (a * (b - 1))
    #this breaks down the multiplication into repeated addition
    return a + multiply(a, b - 1)