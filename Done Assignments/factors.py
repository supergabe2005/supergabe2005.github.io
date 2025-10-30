#Author: Gabriel Gardner
#GitHub username: supergabe2005
#Date: 10/15/25
#Description:takes a positive integer provided by the user, and determines all factorable
#            numbers then, prints factors

#get positive integer
n = int(input("Please enter a positive integer: "))
print(f"The factors of {n} are:")

#loops through all numbers 1 -> n
for i in range(1, n + 1):
    #check if i divided evenly into n %finds remainder
    if n % i == 0:
        #if i is a factor, print
        print(i)