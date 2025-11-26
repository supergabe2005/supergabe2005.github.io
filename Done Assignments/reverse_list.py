#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 11/19/25
#Description: this function reverses the order of elements in
#             a list by swapping elements form the start and end
#             of the list working towards the middle

def reverse_list(items):
    """
    Reverse the order of elements in a list.

    Takes a list and reverses the order of its elements by swapping elements
    from the start and end of the list, working toward the middle. This function
    does not return anything - only indexing is used to grab and swap elements

    args:
    items: A list of any elements to be reversed.

    returns:
    none
    """
    #get the length of the list
    list_length = len(items)

    #loop from the start of the list to the middle
    for i in range(list_length // 2):
        #calculate the index(place) of the element from the end of the list
        opposite_index = list_length - 1 - i

        #store the element at the current start position
        temp = items[i]
        #move the element from the end to the current start position
        items[i] = items[opposite_index]
        #move the stored element from the start position to the end position
        items[opposite_index] = temp