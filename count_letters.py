#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 11/24/25
#Description: This function counts the occurrences of each letter given and returns as a dictionary

def count_letters(text):
    """
    Count the occurrences of each letter in a string and return as a dictionary.

    Takes a string and returns a dictionary where keys are uppercase letters and
    values are the count of how many times that letter appears in the string.
    Only letters are counted; other characters are ignored.

    arg:
    text: A string that may contain letters, numbers, spaces, and special characters.

    returns:
    A dictionary with uppercase letter keys and count values.
    """
    #create an empty dictionary to store letter counts
    letter_counts = {}

    #convert the text to uppercase to handle both cases(A, a)
    text_upper = text.upper()

    #iterate through each character in the string
    for char in text_upper:
        #check if the character is a letter
        if char.isalpha():
            #use the count() method to count occurrences of this letter in the text
            count = text_upper.count(char)
            #add/update the dictionary entry for this letter
            letter_counts[char] = count

    #return the dictionary of letter counts
    return letter_counts