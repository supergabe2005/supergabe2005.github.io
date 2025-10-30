#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/29/25
#Description: This file contains a function definition that calculates the
#             median of a list of numbers whether the list is an even or odd
#             amount in length

def find_median(numbers):
    """
    Calculate the median of a list of numbers.

    The median is the middle value in a sorted list. Odd-length lists,
    it is the middle element. Even-length lists, it is the average of
    the two middle elements.

    Args:
    numbers: A list of numeric values (int or float).

    Returns:
    The median value as a float or int.
    """
    sorted_numbers = sorted(numbers)
    list_length = len(sorted_numbers)

    #calculate the median based on list length odd or even
    if list_length % 2 == 1:
        #odd length: return the middle element
        middle_index = list_length // 2
        median = sorted_numbers[middle_index]
    else:
        #even length: return average of the middle two
        middle_index_1 = list_length // 2 - 1
        middle_index_2 = list_length // 2
        median = (sorted_numbers[middle_index_1] + sorted_numbers[middle_index_2]) / 2

    return median