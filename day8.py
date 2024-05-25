"""
Variables and Datatypes
Basic Understanding:
1. Define a variable student_name and assign it your name.
2. Define a variable student_age and assign it your age.
3. Print both variables in a sentence.
"""
student_name = "Alex"
student_age = 13
# print(f'my name is {student_name} and I am {student_age} years old')

"""
Application:
Write a Python program to convert a temperature from Celsius to Fahrenheit. The formula is:
    Fahrenheit=Celsius×(9/5)+32
"""
def CtoF(temp):
    return temp * (9/5) + 32

# print(CtoF(25))
"""
Problem-Solving:
Write a Python program to swap the values of two variables.
"""

def swap(x, y):
    temp = x
    x = y
    y = temp
    return f'x is {x} and y is {y}'

# print(swap(3, 5))

"""
Operators
Basic Understanding:
1. Define two variables a = 10 and b = 20. Write expressions to:
    > Add, subtract, multiply, and divide a and b.
    > Check if a is less than b.
"""
a, b = 10, 20
# print(a + b, a - b, a * b, a / b)
# print(a < b)
"""    
Application:
Write a Python function to calculate the area and perimeter of a rectangle. 
The length and width should be provided by the user.
"""
def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * length + 2 * width

"""
Problem-Solving:
Write a Python function to check if a given number is divisible by both 5 and 7.
"""
def divBy5and7(x):
    return x % 35 == 0

# print(divBy5and7(141))

"""
Conditionals
Basic Understanding:
Write a Python program that takes an integer input and prints whether the number is positive, negative, or zero.
"""
def posOrNeg(x):
    if(x > 0):
        return "positive"
    elif(x == 0):
        return "zero"
    else:
        return "negative"

"""
Problem-Solving:
Write a Python program that asks the user to 
enter a number between 1 and 7 and 
prints the corresponding day of the week (1 for Monday, 2 for Tuesday, etc.).
"""
def dayOftheWeek(num):
    if(num == 1):
        return "Monday"
    if(num == 2):
        return "Tuesday"
    if(num == 3):
        return "Wednesday"
    if(num == 4):
        return "Thursday"
    if(num == 5):
        return "Friday"
    if(num == 6):
        return "Saturday"
    return "Sunday"

# print(dayOftheWeek(5))

"""
Loops
Basic Understanding:
    Write a Python program to print numbers from 1 to 10 using a for loop.

for i in range(start, end): i is gonna run from start to end - 1
    body

for in range(end): i is gonna run from 0 to end - 1
    body
"""
# for i in range(10): 
#     if i == 9:
#         print(i + 1)
#     else:
#         print(i + 1, end = ", ")

def countMtoN(m, n): 
    # try to print out numbers from m to n, inclusive
    for i in range(m, n + 1): #i : m to n
        if(i == n):
            print(i)
        else:
            print(i, end = ", ") 

# countMtoN(2, 6)

"""
Application:
Write a Python program to calculate the factorial of a given number using a while loop.

n! = 1 * 2 * ... n - 2 * n - 1 * n

while(condition):
    body
"""

def factorial(n):
    result = 1
    # for i in range(1, n + 1):
    #     result = result * i

    while(n >= 1):
        result = result * n
        if(n == 1):
            print(n)
        print(f'{n} ', end = "* ")
        n -= 1

    return result

# print(factorial(10) == 3628800)



"""
Problem-Solving:
Write a Python program to print the first 10 Fibonacci numbers.

1, 1, 2, 3, 5, 8, 13, 21, ...
f(i) = f(i - 1) + f(i - 2)
"""

# num1 = 1
# num2 = 1
# print(f"{num1} {num2}", end = " ")
# for i in range(3, 11): 
#     print(num1 + num2, end = " ")
#     temp = num2
#     num2 = num1 + num2
#     num1 = temp

# for c in "Jeehoon":
#     print(c)

string_value = "sungbin"
# print(string_value[-3])

"""
Strings
1. Basic Understanding:
● Create a string variable with the value "Hello, Python!". Print the comma by accessing the index of the string."""

string_value = "Hello, Python!"
# print(string_value[5], string_value[-9])

"""
2. Application:
● Write a Python program that takes a string input from the user and counts the
number of vowels in the string.
"""
def countVowels(s):
    count = 0
    for c in s:
        if c in "aeiou":
            count += 1
    return count

# print(countVowels("abcdefgaaaeeeiii"))
"""
3. Problem-Solving:
● Write a Python program to reverse a given string.
"""

def reverseString(s):
    result = ""
    for i in range(-1, -1 * len(s) - 1, -1):
        result += s[i]
    return result 

# print(reverseString("Jeehoon, Sungbin, Alex, Hyungjoon"))

"""
Lists
"""
# 1. Creating Lists
# Two ways to create an empty list
# a = []
# b = list()

# print(a)  # Output: []
# print(b)  # Output: []
# print(a == b)  # Output: True

# a = ["hello"]
# b = [42]

# print(a)  # Output: ['hello']
# print(b)  # Output: [42]

# a = [2, 3, 5, 7]
# b = list(range(5))
# c = ["mixed types", True, 42]

# print(a)  # Output: [2, 3, 5, 7]
# print(b)  # Output: [0, 1, 2, 3, 4]
# print(c)  # Output: ['mixed types', True, 42]

# 2. Accessing Elements

# Indexing

# a = [2, 3, 5, 7, 11, 13]

# print(a[0])  
# print(a[2])  
# print(a[-1])
# print(a[-3])  

# # Slicing
# # print(a[0:2])  # Output: [2, 3]
# # print(a[1:4])  # Output: [3, 5, 7]
# # print(a[1:6:2])  # Output: [3, 7, 13]
# print(a[::])

# listname[start :end (exclusive): step]


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[:3])
# print(a[1::2])
# print(a[::-1])

# a = [10, 20, 30, 40, 50, 60, 70]
# # print(a[-5:-1])
# print(a[-1:-6:-2])

# Adding Elements
a = [2, 3]
a.append(7)
print(a)

# Extend Lists
a = [2, 3]
a += [11, 13]
print(a)  # Output: [2, 3, 11, 13]

# Remove Elements
a = [2, 3, 5, 3, 7]
a.remove(3)
print(a)
