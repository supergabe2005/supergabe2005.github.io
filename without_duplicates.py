#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/29/25
#Description:

def without_duplicates(input_list):
    """
    Remove duplicate values from a list while preserving order.

    Takes a list and returns a new list containing all the same values
    but with duplicates removed, in the order of their first appearance
    in the original list. The original list remains unchanged.

    Args:
    input_list: A list that may contain duplicate values.

    Returns:
    A new list with all duplicate values removed. Ordered in
    the original lists way.
    """
    #initialize list
    unique_values = []
    #adds values to new list if not already added
    for value in input_list:
        if value not in unique_values:
            unique_values.append(value)

    return unique_values