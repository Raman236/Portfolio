# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:54:10 2021

@author: Raman Sewjugath
"""
print("Task 2")

# initialize variables and request user input
number = int(input("Please enter an integer: "))

# count is used to keep track of the numbers that have no remainder.
count = 1  

# it is assumed that 1 can go into any number, so count = 1. as well as the entered number
# can go in itself with no remainder, so this will me incremented by 1 later on
# hence count will have value of 2. 

# Checks that the number entered is not 1, it should be greater
if (number > 1):

    # iterates the modulus function of each number from 2 to the entered number                        
    for y in range(2,number+1):         
            if (number % y == 0):

                # if number has no remainder, count will increase by 1      
                count +=1               
    
    # Checks if count is not greater than 2 (Any prime numbers will make this statement True, inializing it)
    if (count <= 2):
        result = f"{number} is a Prime Number"
        print(result)
    
    # if any other numbers have no remainder then the value
    # of count will increase as well as proving count <= 2, false, 
    # initializing the else statement
    else:
        result = f"{number} is NOT a Prime Number"
        print(result)
                      
# if the integer entered is 1, the else statement will be initialized
else:
    print("The number you entered is not greater than 1")