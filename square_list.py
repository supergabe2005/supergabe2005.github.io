#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 11/19/25
#Description: This function takes a list of numbers and replaces
#             each value in the list with the square of that value

def square_list(n):
    """
    Replace each value in a list with the square of that value.

    Takes a list of numbers and mutates it, replacing each element
    with its square. This function does not return anything

    args:
    n(numbers): A list of numeric values (int or float) to be squared.

    returns:
    none
    """
    #iterate through each value/index in the list
    for i in range(len(n)):
        #square the element at index i and assign it back to the same position
        n[i] = n[i] ** 2