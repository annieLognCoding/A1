# HW
"""
1. Basic for Loop
    Suppose you want to write a program that prints numbers from 1 to 10, formatted like this:
    Current value: 1
    Current value: 2
    ...
    Current value: 10

    How can you do that?
    
    Teo: write me a function that takes in two integers and gives me the sum of all integers in between (exclusive)
    def sumMtoN(m, n):
"""

# for i in range(1, 11):
#     print(f"Current value: {i}")

# difference between for-loop and while-loop

# i = 1
# while(i < 11):
#     print(f"Current value: {i}")
#     i += 1

# print(f"The value of i is now: {i}")

# 1. Given the nested if-else structure below, 
# what will be the value of x after code execution completes

# x = 0
# a = 0
# b = -5

# if a == 0:
#     if b < 0: 
#         x = x + 5 #x = 5
#     if a < 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)


# 2. What is the value of x

# x = 0
# while (x <= 10): # x > 10
#   x+=2

# print(x)

# 3. Given the nested if-else below, what will be the value x when the code executed successfully

# x = 0
# a = 5
# b = 5
# if a > 0:
#     if b < 0: 
#         x = x + 5 
#     elif a >= 5:
#         x = x + 4 #4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

# 4. What is the output of the following for loop and  range() function

# for num in range(-2,-5,-1):
#     print(num, end=", ")

# 5. What is the output of the following range() function

# for num in range(2,-5,-1):
#     print(num, end=", ")

# for num in range(-5, 2, 2):
#     print(num, end=", ")

# 6. What is the output of the following if statement

# a, b = 12, 5
# if a + b > 17:
#     print('Seventeen')
# elif a - b >= 7:
#     print('Seven')
# else:
#     print('None')

# Nested Loops!

"""
Nested loops mean loops inside a loop. 
For example, while loop inside the for loop, for loop inside the for loop, etc.
"""

# for i in range(0, 4): #i = 0, 1, 2, 3
#     print(f'{i}: ')
#     for j in range(10): #j = 0 - 9
#         if j < 9:
#             print(i * 10 + j, end = ", ")
#         else:
#             print(i * 10 + j, end = " ")
#     print()


# Python Nested Loop Syntax
"""
Outer_loop Expression: (1 - 10)
    Inner_loop Expression: (1 - 10)
        Statement inside inner_loop
    Statement inside Outer_loop
"""

# Example 1: Basic Example of Python Nested Loops

# for i in range(1, 3): #i = 1, 2
#     for j in range(4, 6): #j = 4, 5
# 	    print(i, j)
          
# Running outer loop from 2 to 3
 
# for i in range(2, 4): #i = 2, 3
 
#     # Printing inside the outer loop
#     # Running inner loop from 1 to 5
#     for j in range(1, 6): #j = 1~5
 
#         # Printing inside the inner loop
#         print(i, "*", j, "=", i*j, end=", ") #2 * 1 = 2, 2 * 2 = 4, 2 * 3 = 6, 2*4 = 8, 2 * 5 = 10
#     # Printing inside the outer loop
#     print()

#Send in email and go to break until 2:07

# Running outer loop from 2 to 3
# for i in range(2, 4): #i = 2, 3
#     # Printing inside the outer loop
#     # Running inner loop from 1 to 5
#     for j in range(1, 6): #j = 1 ~ 5
#       if i==j:
#         break
#       # Printing inside the inner loop
#       print(i, "*", j, "=", i*j)
#     # Printing inside the outer loop
#     print()

# What is the output of the following code?

# total = 0
# for num in range(1, 6): #num = 1, 2, 3, 4, 5
#    total = total + num
# print(total)

# # What will the following code output?

# for i in range(3): #i = 0, 1, 2
#    for j in range(2): # j = 0, 1
#        print(i, j)
       
# What is the value of the var after the for loop completes its execution

# var = 10
# for i in range(5): #i = 0, 1, 2, 3, 4
#     print(var, end = ", ")
    
#     for j in range(2, 6, 1): #j = 2, 3, 4
#         if var % 2 == 1:
#             var += 1
#         else:
#             var -= 1
    
#     var += 1
#     print()

# print(var)

"""Strings"""

# for i in "alex, jeehoon":
#     print(i)


# string_1 = "Alex, Jeehoon"
# for i in range(len(string_1)): #i = 0 - 12
#     print(string_1[i], end=" ")

string_a = "Hyungjoon"
string_b = "Teo"
print(string_a[2], string_b[2])