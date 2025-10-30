#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/8/25
#Description: This program converts an amount of cents (less than a dollar(0–99)
#             into the fewest number of coins.

print("Please enter an amount in cents less than a dollar.")

#get user input and convert to integer
cents = int(input())

#calculate number of quarters
quarters = cents // 25
cents = cents % 25

#calculate number of dimes
dimes = cents // 10
cents = cents % 10

#calculate number of nickels
nickels = cents // 5
cents = cents % 5

#remaining cents are pennies
pennies = cents

#output results
print("Your change will be:")
print("Q:", quarters)
print("D:", dimes)
print("N:", nickels)
print("P:", pennies)
