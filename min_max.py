#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/14/25
#Description: Prompts the user for () amount of integers, then finds min and max of
#             of listed integers and displays the min and max

#define n, and prompt user
n = int(input("How many integers would you like to enter? "))
print(f"Please enter {n} integers.")

#read the first integer and initialize min and max
num1 = int(input())
min_val = num1
max_val = num1

#read the remaining integers
for i in range(1, n):
    num = int(input())
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print(f"min: {min_val}")
print(f"max: {max_val}")