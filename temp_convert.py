#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/8/25
#Description: This program converts Celsius to Fahrenheit using the formula: F = (9/5) * C + 32

print("Please enter a Celsius temperature.")

#get user input and convert to float
celsius = float(input())

#calculate fahrenheit
fahrenheit = (9 / 5) * celsius + 32

#display result
print("The equivalent Fahrenheit temperature is:")
print(fahrenheit)
