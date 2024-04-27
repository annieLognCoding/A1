# meet.google.com/tiu-gnjc-nnq


# def shout(x):
#     print("Hi, " + str(x) + "!")

# shout(43)

# def round(x):
#     print(int(x + 0.5)) #how to fix this?

#Functions Review
# def func1(x, y, z):
#     t = y - x #1
#     a = t + z #2
#     return a

# b = func1(2, 3, 1)
# print(b)


# def func2(x):
#     return (x % 100) // 10 

# print(func2(12345), func2(1111), func2(1212))
# def func3(x, y, z):
#     print("hi, " + str(x) + "!")
#     print(y == z) 
#     return x > z

# print(func3(12, 23, 23))

# def func4(x):
#     print(x * 5)

# print(func4(2))


#Challenge!
# def funcky(x): #x = 5324
#     temp = len(str(x)) - 1 #temp = 3
#     return x // (10 ** temp) #5324 // 1000

# print(funcky(5324), funcky(-3234123))


#8. Scope

# 8 - 1: Local Variable Scope
#The scope of local variables are bound within 
#the block where they were instantiated 

# def f(x):
#     print("In f, x =", x) #x = 6
#     x += 5 # 11
#     return x # 11

# def g(x): #x = 2
#     a = f(x*2) #9
#     b = f(x * 3) #11
#     return a + b #20

# print(g(2))

# def f1(x): #20
#     print("In f, x =", x) #print
#     x = x + 7 #x = 27
#     return int(x / 3) #9

# def g1(x): #x = 2
#     x = x * 10 #x = 20 
#     return 2 * f1(x) #18

# print(g1(2))

# def h(x):
#     x += 3
#     return f1(x+4) + g1(x)

# print(h(f1(1)))

# # 8 - 2: Global Variable Scope

# # In general, you should avoid using global variables.
# # You will even lose style points if you use them!
# # Still, you need to understand how they work, since others
# # will use them, and there may also be some very few occasions
# # where you should use them, too!

# g = 100

# def f(x):
#     return x + g

# print(f(5)) # 105
# print(f(6)) # 106
# print(g)    # 100

# g = 100

# def f(x):
#     # If we modify a global variable, we must declare it as global.
#     # Otherwise, Python will assume it is a local variable.
#     global g
#     g += 1
#     return x + g

# print(f(5)) # 106
# print(f(6)) # 108
# print(g)    # 102

# #Chapter 3: More About Data and Expressions

# #1. Some Built-in Functions
# print("Type conversion functions:")
# print(float(42)) # convert to a floating point number
# print(int(2.8))  # convert to an integer (int)
# print(3 == 3) 
# print(3 != 3)

# print("And some basic math functions:")
# print(abs(-5))   # absolute value
# print(max(2,3))  # return the max value
# print(min(2,3))  # return the min value
# print(pow(2,3))  # raise to the given power (pow(x,y) == x**y)
# print(round(2.354, 1)) # round with the given number of digits

# #2. Some Built-in Operators

# """
# Category  | Operators              |

# Arithmetic| +, -, *, /, //, **, %  |

# Relational| <, <=, >=, >, ==, !=   |

# Assignment| =, +=, -=, *=, /=, //= |

# Logical   | and, or, not           |
# """

x = 5
print(x)
x += 5 # x = x + 5
print(x) 
x -= 5 
print(x) #x = 5
x *= 5
print(x) 
x /= 3 
print(x) 
x = int(x) 
x //= 3
print(x)

# y = 10

# print(x >= y)
# print(x <= y)
# print(x != y)
# print(x == y)

#3. Types Affect Semantics

# print(3 * 2)
# print(3 * "abc")
# print(3 + 2)
# print("abc" + "def")
# print(str(3) + "def")

# #4. Integer Division
# print("The / operator does 'normal' float division:")
# print(" 5/3  =", ( 5/3))
# print()
# print("The // operator does integer division:")
# print(" 5//3 =", ( 5//3))
# print(" 2//3 =", ( 2//3))
# print("-1//3 =", (-1//3))
# print("-4//3 =", (-4//3))

# #5. The Modulus or Remainder Operator (%)
# print(" 6%3 =", ( 6%3))
# print(" 5%3 =", ( 5%3))
# print(" 2%3 =", ( 2%3))
# print(" 0%3 =", ( 0%3))
# print("-4%3 =", (-4%3))
# print(" 3%0 =", ( 3%0))

# #What if we didn't have a modulo operator?

# """
# def mod(a, b):
#     how do we define modulo with just //, * and -?
# """

# #6. Order of Operations
# print("Precedence:")
# print(2+3*4)  # prints 14, not 20
# print(5+4%3)  # prints  6, not 0 (% has same precedence as *, /, and //)
# print(2**3*4) # prints 32, not 4096 (** has higher precedence than *, /, //, and %)

# print()

# print("Associativity:")
# print(5-4-3)   # prints -2, not 4 (- associates left-to-right)
# print(4**3**2) # prints 262144, not 4096 (** associates right-to-left)


# #QUICK REVIEW OF LOGICAL OPERATORS!
# """
# A | B | A OR B | A AND B |
# F | F |   F    |    F    |
# F | T |   T    |    F    |
# T | F |   T    |    F    |
# T | T |   T    |    T    |
# """
# #7. Short-Circuit Evaluation
# def yes():
#     return True

# def no():
#     return False

# def crash():
#     return 1/0 # crashes!

# print(no() and crash()) # Works!
# print(crash() and no()) # Crashes!
# print (yes() and crash()) # Never runs (due to crash), but would also crash (without short-circuiting)

# def yes():
#     return True

# def no():
#     return False

# def crash():
#     return 1/0 # crashes!

# print(yes() or crash()) # Works!
# print(crash() or yes()) # Crashes!
# print(no() or crash())  # Never runs (due to crash), but would also crash (without short-circuiting)

#Chapter 4: Conditionals

# 1. if Statement
def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    if (x == 1):
        print("D", end="")
    print("D")

f(0)
f(1)

# # These examples define abs(n), which is a nice example here, but it is
# # also a builtin function, so you do not need to define it to use it.

# def abs1(n):
#     if (n < 0):
#         n = -n
#     return n

# again, with same-line indenting

# def abs2(n):
#     if (n < 0): n = -n # only indent this way for very short lines (if at all)
#     return n

# # again, with multiple return statements

# def abs3(n):
#     if (n < 0):
#         return -n
#     return n

# # aside: you can do this with boolean arithmetic, but don't!

# def abs4(n):
#     return (n < 0)*(-n) + (n>=0)*(n) # this is awful!

# # now show that they all work properly:

# print("abs1(5) =", abs1(5), "and abs1(-5) =", abs1(-5))
# print("abs2(5) =", abs2(5), "and abs2(-5) =", abs2(-5))
# print("abs3(5) =", abs3(5), "and abs3(-5) =", abs3(-5))
# print("abs4(5) =", abs4(5), "and abs4(-5) =", abs4(-5))

#2. if-else Statement
def f(x): #x = 2
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    else:
        print("D", end="")
        if (x == 1):
            print("E", end="")
        else:
            print("F", end="")
    print("G")

f(0)
f(1)
f(2)

# #Revisiting abs(n):
# def abs5(n):
#     if (n >= 0):
#         return n
#     else:
#         return -n

# # or, if you prefer...

# def abs6(n):
#     if (n >= 0):
#         sign = +1
#     else:
#         sign = -1
#     return sign * n

# print("abs5(5) =", abs5(5), "and abs5(-5) =", abs5(-5))
# print("abs6(5) =", abs6(5), "and abs6(-5) =", abs6(-5))

#3. if-elif-else statement
def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    elif (x == 1):
        print("D", end="")
    else:
        print("E", end="")
        if (x == 2):
            print("F", end="")
        else:
            print("G", end="")
    print("H")

f(0)
f(1)
f(2)
f(3)

# #Another example
# def numberOfRoots(a, b, c):
#     # Returns number of roots (zeros) of y = a*x**2 + b*x + c
#     d = b**2 - 4*a*c
#     if (d > 0):
#         return 2
#     elif (d == 0):
#         return 1
#     else:
#         return 0

# print("y = 4*x**2 + 5*x + 1 has", numberOfRoots(4,5,1), "root(s).")
# print("y = 4*x**2 + 4*x + 1 has", numberOfRoots(4,4,1), "root(s).")
# print("y = 4*x**2 + 3*x + 1 has", numberOfRoots(4,3,1), "root(s).")

#Another example
def getGrade(score):
    if (score >= 90):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    else:
        grade = "F"
    return grade

print("103 -->", getGrade(103))
print(" 88 -->", getGrade(88))
print(" 70 -->", getGrade(70))
print(" 61 -->", getGrade(61))
print(" 22 -->", getGrade(22))

def max(a, b):
    if(a >= b):
        return a
    else:
        return b
    #the larger number, if a and b are the same, just return a

def sum(a, b):
    sum = a + b
    if a == b:
        return 2 * sum
    else:
        return sum
    #return the sum of a and b, except if a is equal to b, double their sum
max(3, 5)
max(4, 2)
