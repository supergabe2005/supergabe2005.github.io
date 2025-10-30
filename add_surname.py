#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/29/25
#Description: This file contains a function definition that takes a list of
#             names and determines whether a name starts with a 'K', if so
#             the function will add the surname "Kardashian" to it.

def add_surname(first_names):
    """
    Filter names starting with "K" and add "Kardashian" as a surname.

    Takes a list of first names and returns a new list containing only
    those names that start with the letter "K", with "Kardashian" appended
    as a surname.

    Args:
    first_names: A list of first names (strings).

    Returns:
    A list of names in the format "FirstName Kardashian".
    """
    #If the first name begins with 'K' add 'Kardashian'
    kardashian_names = [name + " Kardashian" for name in first_names
                        if name[0] == "K"]

    return kardashian_names