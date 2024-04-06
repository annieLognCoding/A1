import math

##Primitive data types
def f():
    print("This is a user-defined function")
    return 42

print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float
print(type("2.2"))       # str  (string)
print(type(2 < 2.2))     # bool (boolean)


##Casting

large_float = 1.7e308  # This is a very large float
large_int = int(large_float)  # Works in Python, but the fractional part is lost
print(large_float, large_int)

print(float(10))
print(int(9.8))
print(int("3"), float("4.2"))
print(str(5), str(3.14))

print(3 + 3)
print("3" + "3")
print(3 + "3")

number = "3"
# print(3 + number)			# Type Error!
print(number)
print(type(number))
print(type(int(number)))		# only integer in this instance
number = int(number)
print(3 + number)


#Complex Data Types
print(type(math))        # module
print(type(math.tan))    # builtin_function_or_method ("function" in Brython)
print(type(f))           # function (user-defined function)
print(type(type(42)))    # type
print(type(Exception())) # Exception
print(type(range(5)))    # range

print(type([1,2,3]))     # list
print(type((1,2,3)))     # tuple
print(type({1,2}))       # set
print(type({1:42}))      # dict (dictionary or map)
print(type(2+3j))        # complex  (complex number) (we may not see this type)

#Data Structures
listA = [1, 2, 3]
tupleA = (1, 2, 3)
str = "abcd"

listA[0] = 2
print(listA[0])

#immutable objects! Illegal!
# tupleA[0] = 1
# str[0] = "b"

setA = set((1, 2, 3, 4, 3, 4, 4))
print(setA)

#naming conventions:
b = None #single lowercase letter
B = None #single uppercase letter
lowercase = None 
lower_case_with_underscores = None
UPPERCASE = None
UPPER_CASE_WITH_UNDERSCORES = None
CapitalizedWords = None #or CapWords, or CamelCase
mixedCase = None #also usually called camelcase 
Capitalized_Words_With_Underscores = None #ugly!
digits0can1be2used = None 
#0thisisbad

# # Variable 
a = 10 
b = 7 
print(a + b)
b = 5 
print(a + b)

print(a == b)

#pass by value, pass by reference

def switchNo(x, y):
    temp = x
    x = y
    y = temp

a = 3
b = 5
switchNo(a, b)
print(a, b)


def switch(x, y):
    temp = x["v"]
    x["v"] = y["v"]
    y["v"] = temp

a = {"v": 3}
b = {"v": 5}
switch(a, b)
print(a, b)


# # Operator 
# print(1 + 1) 	# addition 
# print(5 - 3) 	# subtraction 
# print(10 * 7)	# multiplication 
# print(10 // 7)	# whole number division (quotient)
# print(10 / 7)	# exact value division 
# print(10 % 7)	# Modular --> Remainder 
# print(10 ** 3)	# Exponent 
# print(10 > 3)
# print(10 >= 3)
# print(10 == 3)	# False 
# print(10 != 3)	# True (! means NOT)




## Functions ## 

### x + 1 doesn't actually increase value of x. 
### You have to reassign it by x = x+ 1 

# x = 10 
# print(x)
# print(x + 1)
# x = x + 1
# print(x)

# Function is composed of 3 parts: input (ingredient), body (function), return 

# Return is used inside a function only. Can't be used outside of function
# Return stores the value whereas print is only used for scanning errors (debugging)
# Print is useful later for debugging and placing checkpoints 
# Always use return for now in functions 


def addOne(number):
	number = number + 1 
	return number 

# print(addOne(5))


def digitAdd(number): 
	firstDigit = number // 10 
	secondDigit = number % 10 
	return firstDigit + secondDigit

# print(digitAdd(67))


### Conditionals ### 
# x = 5 
# if x < 3: 
# 	print("YAY")

# print("YAY2")

# scopes are identified by indents 

# else
# x = 5 
# if x < 3: 
# 	print("YAY")
# else: 
# 	print("NAY")


# elif 
# 50 boys, 50 girls 
# 20 boys wearing black shirt 
# 30 girls wearing black shirt 

# if, if 
# if you are a boy wearing black shirt raise your hand
# if you are a boy raise your hand --> 50 
# the boys wearing black shirt are INCLUDED in the 2nd question 

# if, elif (else if)
# if you are a boy wearing black shirt go home 
# if you are a boy raise your hand --> 30 
# the boys wearing black shirt are EXCLUDED in the 2nd question 


# 1. given a number, return whether the number is an odd number 
# 2. given a number, return the absolute value of the number 
# 3. given number a and b, return whether one is a factor of the other 
# 4. given 3 sides, return whether you can form a legal triangle  


# 1. 
def oddEven(num): 
	if num % 2 == 1: # if remainder 1 when divided by 2 
		return "Odd"
	else: 
		return "Even"

print(oddEven(3))		 


#2. 
def absVal(num): 
	if num < 0: 
		return num * -1 
	else: 
		return num 

	# abs(num)

num = -17 
print(abs(num))



def isFactor(a, b): 
	if a % b == 0: 
		return True 
	if b % a == 0: 
		return True 
	else: 
		return False 

	# return a % b == 0 or b % a == 0

print(isFactor(3, 9))



def isLegalTriangle(a, b, c): 
	perimeter = a + b + c 
	return 


print(max(1,2,3,4,5))
print(min(3,6,17))



## Extra Practice 

#1. The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
  return not weekday or vacation

#2. Write the function getKthDigit(n, k) that takes a possibly-negative int n 
# and a non-negative int k, and returns the kth digit of n, starting from 0, 
# counting from the right. So:

# getKthDigit(789, 0) == 9
# getKthDigit(789, 1) == 8
# getKthDigit(789, 2) == 7
# getKthDigit(789, 3) == 0
# getKthDigit(-789, 0) == 9
