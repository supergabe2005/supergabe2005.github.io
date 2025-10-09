#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/8/25
#Description: this program asks the user for five numbers and prints their average.

print("Please enter five numbers.")

#get input from user and convert each to float
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())

#calculate average
average = (num1 + num2 + num3 + num4 + num5) / 5

#print result
print("The average of those numbers is:")
print(average)
