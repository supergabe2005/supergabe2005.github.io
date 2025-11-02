#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 11/2/25
#Description: The word_length_std_dev function calculates the sample
#             standard deviation of word lengths in a given string.

def word_length_std_dev(text):
    """
    Calculate the sample standard deviation of word lengths in a string

    Args:
    text: A string containing words separated by spaces

    Returns:
    The sample standard deviation of word lengths
    """
    #split text into words
    words = text.split()

    #error case: less than 2 words (can't calculate sample std dev)
    if len(words) < 2:
        return None

    #calculate word lengths
    word_lengths = [len(word) for word in words]

    #calculate mean
    mean = sum(word_lengths) / len(word_lengths)

    #calculate squared differences from mean
    squared_diffs = [(length - mean) ** 2 for length in word_lengths]

    #sum squared differences
    sum_squared_diffs = sum(squared_diffs)

    #divide by (N - 1) for sample standard deviation
    variance = sum_squared_diffs / (len(word_lengths) - 1)

    #take square root
    std_dev = variance ** 0.5

    return std_dev


#Test cases(Not as expected)
#if __name__ == "__main__":
    # Test 1: All words equal length
    text1 = "cat dog bird"
    result1 = word_length_std_dev(text1)
    print(f"Test 1: '{text1}'")
    print(f"Result: {result1}")
    print(f"Expected: 0.0\n")

    # Test 2: Complex sentence with varied word lengths
    text2 = "There is wisdom in turning as often as possible from the familiar to the unfamiliar it answer"
    result2 = word_length_std_dev(text2)
    print(f"Test 2: '{text2}'")
    print(f"Result: {result2}")
    print(f"Expected: ~2.44\n")