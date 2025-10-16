#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/15/25
#Description:prompts user for an integer, then the user must guess the integer entered,
#            the code counts how many guesses, and displays the guess count once guessed correctly

#get target integer from user
target = int(input("Enter the integer for the player to guess.\n"))

#initialize the guess counter
guesses = 0

#keep looping until the player guesses correctly
while True:
    #get the players guess
    guess = int(input("Enter your guess.\n"))

    #increment
    guesses = guesses + 1

    #check if the guess is too high
    if guess > target:
        print("Too high - try again:")
    #check if the guess is too low
    elif guess < target:
        print("Too low - try again:")
    #the guess is correct
    else:
        break

#check if it took only 1 try
if guesses == 1:
    print("You guessed it in 1 try.")
else:
    print(f"You guessed it in {guesses} tries.")