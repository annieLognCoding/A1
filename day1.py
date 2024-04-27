import math

##Primitive data types

# print("Some basic types in Python:")
print(type(2))           # 
print(type(2.2))         # 
print(type("2.2"))       # 
print(type(2 < 2.2))     # 

#types: int, float (decimal), str (text), bool (true or false)

##Casting

print({float(10), float(5), float(6)}) #
print(int(9.8)) #
print("3" + "4.2") 

print(str(5) + " says hi", str(3.14))
print(3 + 3)
print("3" + "3")
print(3 + int("3"))
print(str(3) + "3")


number = "3" #assignment
print("43" + number)			
print(number)
print(type(number)) #str
print(type(int(number)))		# only integer in this instance

number = "44"
print(type(number))
number = int(number)
# print(3 + number)


# #Complex Data Types

def f():
    print("This is a user-defined function")
    return 42


# print(type(f))           # function (user-defined function)

# print(type(type))    # type

# print(type([1,2,3]))     # list mutable = changed
# print(type((1,2,3)))     # tuple immutable = cannot be changed
# print(type({1,2}))       # set only one element of the same value can be stored

# print(type({1:42}))      # dict (dictionary or map)
# print(type(2+3j))        # complex  (complex number) (we may not see this type)

# #Data Structures
# listA = [1, 2, 3]
# tupleA = (1, 2, 3)
# str = "abcd"

# listA[0] = 2
# print(listA[0])

# #immutable objects! Illegal!
# # tupleA[0] = 1
# # str[0] = "b"

# setA = set((1, 2, 3, 4, 3, 4, 4))
# print(setA)

# #naming conventions:
# b = None #single lowercase letter
# B = None #single uppercase letter
# lowercase = None 
# lower_case_with_underscores = None
# UPPERCASE = None
# UPPER_CASE_WITH_UNDERSCORES = None
# CapitalizedWords = None #or CapWords, or CamelCase
# mixedCase = None #also usually called camelcase 
# Capitalized_Words_With_Underscores = None #ugly!
# digits0can1be2used = None 
# #0thisisbad

# # Variable 
a = 5
x = True
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Initialize a variable named "false" with the int value 0
false = 0
# Initialize a variable name "hi" with the string value "Hello"
hi = "Hello"
# Initialize a variable name "colors" with a list that contains 3 strings that each represents a favorite color
colors = ["red", "white", "blue"]

#Initialize a variable named "integers" with a tuple of 2 different strings
integers = ("a", "b")

# print(a == b)

# #pass by value, pass by reference

# def switchNo(x, y):
#     temp = x
#     x = y
#     y = temp

# a = 3
# b = 5
# switchNo(a, b)
# print(a, b)


# def switch(x, y):
#     temp = x["v"]
#     x["v"] = y["v"]
#     y["v"] = temp

# a = {"v": 3}
# b = {"v": 5}
# switch(a, b)
# print(a, b)


# # Operator 
print(1 + 1) 	# addition 
print(5 - 3) 	# subtraction 
print(10 * 7)	# multiplication 
print(10 // 7)	# whole number division (quotient)
print(10 / 7)	# exact value division 
print(10 % 7)	# Modular --> Remainder 
print(10 ** 3)	# Exponent 10^3

print(3 + 27 % 4) # % has the same order of precedence as * and /
print(30 // 4)

##boolean = True (1) or False (0)
print(10 > 3)
print(10 >= 3)    # greater than or equal to <=
print(10 == 3) 
print(10 != 3)	

# ## Functions ## 

# define a function that takes in an int and 
# returns the the last digit

# %, //
def lastDigit(n):
    return n % 10

def firstDigit(n):
    fd = n
    while fd >= 10:
        fd //= 10 
    return fd

def sumDigits(n):
    return firstDigit(n) + lastDigit(n)




# ### x + 1 doesn't actually increase value of x. 
# ### You have to reassign it by x = x+ 1 

# # x = 10 
# # print(x)
# # print(x + 1)
# # x = x + 1
# # print(x)

# # Function is composed of 3 parts: input (ingredient), body (function), return 

# # Return is used inside a function only. Can't be used outside of function
# # Return stores the value whereas print is only used for scanning errors (debugging)
# # Print is useful later for debugging and placing checkpoints 
# # Always use return for now in functions 


# def addOne(number):
# 	number = number + 1 
# 	return number 

# # print(addOne(5))


# def digitAdd(number): 
# 	firstDigit = number // 10 
# 	secondDigit = number % 10 
# 	return firstDigit + secondDigit

# # print(digitAdd(67))


# ### Conditionals ### 
# # x = 5 
# # if x < 3: 
# # 	print("YAY")

# # print("YAY2")

# # scopes are identified by indents 

# # else
# # x = 5 
# # if x < 3: 
# # 	print("YAY")
# # else: 
# # 	print("NAY")


# # elif 
# # 50 boys, 50 girls 
# # 20 boys wearing black shirt 
# # 30 girls wearing black shirt 

# # if, if 
# # if you are a boy wearing black shirt raise your hand
# # if you are a boy raise your hand --> 50 
# # the boys wearing black shirt are INCLUDED in the 2nd question 

# # if, elif (else if)
# # if you are a boy wearing black shirt go home 
# # if you are a boy raise your hand --> 30 
# # the boys wearing black shirt are EXCLUDED in the 2nd question 


# # 1. given a number, return whether the number is an odd number 
# # 2. given a number, return the absolute value of the number 
# # 3. given number a and b, return whether one is a factor of the other 
# # 4. given 3 sides, return whether you can form a legal triangle  


# # 1. 
# def oddEven(num): 
# 	if num % 2 == 1: # if remainder 1 when divided by 2 
# 		return "Odd"
# 	else: 
# 		return "Even"

# print(oddEven(3))		 


# #2. 
# def absVal(num): 
# 	if num < 0: 
# 		return num * -1 
# 	else: 
# 		return num 

# 	# abs(num)

# num = -17 
# print(abs(num))



# def isFactor(a, b): 
# 	if a % b == 0: 
# 		return True 
# 	if b % a == 0: 
# 		return True 
# 	else: 
# 		return False 

# 	# return a % b == 0 or b % a == 0

# print(isFactor(3, 9))



# def isLegalTriangle(a, b, c): 
# 	perimeter = a + b + c 
# 	return 


# print(max(1,2,3,4,5))
# print(min(3,6,17))



# ## Extra Practice 

# #1. The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
# # sleep_in(False, False) → True
# # sleep_in(True, False) → False
# # sleep_in(False, True) → True

# def sleep_in(weekday, vacation):
#   return not weekday or vacation

# #2. Write the function getKthDigit(n, k) that takes a possibly-negative int n 
# # and a non-negative int k, and returns the kth digit of n, starting from 0, 
# # counting from the right. So:

# # getKthDigit(789, 0) == 9
# # getKthDigit(789, 1) == 8
# # getKthDigit(789, 2) == 7
# # getKthDigit(789, 3) == 0
# # getKthDigit(-789, 0) == 9
