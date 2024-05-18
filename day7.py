import random


def reverse_each_word(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def first_half(text):
    half_index = len(text) // 2
    if len(text) % 2 != 0:
        half_index += 1
    return text[:half_index]

def substrings_between(s, start, end):
    results = []
    parts = s.split(start)[1:]  # Skip the first split as it will not start with start
    for part in parts:
        if end in part:
            results.append(start + part.split(end)[0] + end)
    return results

def contains_xyz(s):
    count = 0
    i = 0
    while i < len(s) - 2:
        if s[i:i+3] == 'xyz':
            if i == 0 or s[i-1] != '.':
                count += 1
        i += 1
    return count

# 1. Variables and Datatypes

"""
Variable: name of a value; 
    space in memory that the computer can refer to

Different data types in Python:
    Primitives: int, float, String, boolean
    Advanced: list, set, dict

Integer vs. Float:
    integer: whole number
    float: decimal

Variable Assignment
    variable_name = value

Type Casting
    converting one data type to another
    float_number = float(5)
"""

age = 25
# Assign variable name fall to the value of "September"
fall = "September"
x = 50
x = str(x)

a = 10
b = 20.5
c = "Hello"
# print(type(a), type(b), type(c))

# concatenating Strings?
x = "hi" + " hello"
# print(x)

name = "Sungbin"
greeting = "Hello"
s = name + " " + greeting
# print(s)

# Operators
"""
1. Mathematical, Logical, Comparison, Assignment
    +-*/%//, (and or not), > < <= >= ==, = += -=

2. x == y and x = y

3. // --> integer division
"""

# x = 5
# y = 3
# print(a > b and b > c)
# print(x ** y)
# print((a + b + c)/3)

def isEven(x):
    return x % 2 == 0 #if x is even or odd

# 1. if x is divisible by 2, we call it even
# 2. if x % 2 == 0, then x is divisible by 2

# print(isEven(5), isEven(14))

def lastDigitOne(x):
    return x % 10 == 1

# x = 123

# if(x % 2 == 0):
#     print(f"{x} is even")
# else:
#     print(f"{x} is odd")

# for i in range(10):
#     x = int(random.random() * 6) + 1

#     if(x < 3):
#         print(f'{x} is less than 3')
#     elif(x < 5):
#         print(f'{x} is 3 or 4')
#     else:
#         print(f'{x} is greater than or equal to 5')


def whatNumber(x):
    if(x > 0):
        return "positive"
    elif(x == 0):
        return "zero"
    else:
        return "negative"
    
print(whatNumber(23))