"""
Homework Questions for Review
Variables and Data Types

Basic Understanding:
Define a variable student_name and assign it your name.
Define a variable student_age and assign it your age.
Print both variables in a sentence.

I am Annie and I'm 28 years old.
"""

student_name = 'Annie'
student_age = 28
print(f'I am {student_name} and I\'m {student_age} years old')



"""
Application:
Write a Python program to convert a temperature from Celsius to Fahrenheit. 
The formula is: Fahrenheit = Celsius * (9/5) + 32
"""

def CtoF(celsius):
    return celsius * (9/5) + 32


"""
Problem-Solving:
Write a Python program to swap the values of two variables without using a temporary variable.
"""

def swap(x, y):
    return [y, x]


"""
Operators
Basic Understanding:
Define two variables a = 10 and b = 20. Write expressions to:
Add, subtract, multiply, and divide a and b.
Check if a is less than b.
"""
a = 10
b = 20

print(a + b, a - b, a * b, a/b)
print(a < b)

"""
Application:
Write a Python program to calculate the area and perimeter of a rectangle. The length and width should be provided by the user.
"""
def area(length, width):
    return length * width

def perimeter(length, width):
    return (length + width) * 2

"""
Problem-Solving:
Write a Python program to check if a given number is divisible by both 5 and 7.
"""

def isDiv5and7(num):
    return num % 7 == 0 and num % 5 == 0

def isDiv5and7_v2(num):
    return num % 35 == 0
"""
Conditionals
Basic Understanding:
Write a Python program that takes an integer input and prints whether the number is positive, negative, or zero.
Application:
Write a Python program to determine if a given year is a leap year.
Problem-Solving:
Write a Python program that asks the user to enter a number between 1 and 7 and prints the corresponding day of the week (1 for Monday, 2 for Tuesday, etc.).
"""
def isPosNegZero(num):
    if num > 0: return 'positive'
    if num < 0: return 'negative'
    return 'zero'

def leapYear(year):
    return year % 4 == 0

def dayOftheWeek():
    num = int(input('Write a number between 1 and 7'))
    if num == 1: return 'Mon'
    #... if num == 7: return 'Sun'

"""
Loops
Basic Understanding:
Write a Python program to print numbers from 1 to 10 using a for loop.
Application:
Write a Python program to calculate the factorial of a given number using a while loop.
Problem-Solving:
Write a Python program to print the first 10 Fibonacci numbers.
"""
for i in range(1, 11):
    print(i)

def factorial(n):
    result = 1
    while(n > 0):
        result *= n
        n -= 1
    return result

a = 1
b = 1

print(a, b, end = " ")
for i in range(8):
    print(a + b, end = " ")
    temp = b
    b = a + b
    a = temp

"""
Strings
Basic Understanding:
Create a string variable with the value "Hello, Python!". Print the string in uppercase.
Application:
Write a Python program that takes a string input from the user and counts the number of vowels in the string.
Problem-Solving:
Write a Python program to reverse a given string.
"""

str1 = 'Hello, Python!'
print(str1.upper())

def countVowels(str1):
    count = 0
    for c in str1:
        if c in 'aeiou':
            count += 1
    return count

def reverseString(str1):
    return str1[::-1]


message = 'hello, world!'


# casting
print(int(3.14))

#variable assignment
variable_name = 'value'

#greet
def greet(name):
    return f'Hello, {name}!'

x = 20
if x < 20:
    print('x is small')
elif x < 40:
    print('x is medium')
else:
    print('x is large')

for i in range(5):
    print(i + 1)

count = 0
while count < 5:
    print(count)
    count += 1

message = 'Hello, World!'
print(message)


str1 = 'Hello'
print(str1[0], str1[-1])

def replaceHJ(str1):
    result = ''
    for c in str1:
        if c == 'h':
            result += 'j'
        else:
            result += c
    return result

print(message[:5], message[7:13], message[::2])

for c in 'Hello':
    print(c)

def even_or_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
fruits = ['strawberry', 'apple', 'blueberry']

for fruit in fruits:
    print(fruit)

fruits.append('banana')
print(fruits)

def isPrime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True
