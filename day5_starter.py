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

i = 1
while(i < 11):
    print(f"Current value: {i}")
    i += 1

print(f"The value of i is now: {i}")

# 1. Given the nested if-else structure below, 
#what will be the value of x after code execution completes

x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)


