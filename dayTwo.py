### Functions ###


# 1. Vocabulary  
x = 5
def f(y, z):
    result = x + y + z
    return result
print(f(1, 2)) # 8
print(f(3, 4)) # 12

# Vocabulary:
#   global variable
#   local variable
#   statement
#   expression
#   function definition (or declaration)
#   function call
#   parameter (or "formal parameter")
#   argument
#   return value
#   return type

#2. Return statements
# Basic example

def isPositive(x):
    return (x > 0)

print(isPositive(5))  # True
print(isPositive(-5)) # False
print(isPositive(0))  # False

# Return ends the function immediately
def isPositive(x):
    print("Hello!")   # runs
    return (x > 0)
    print("Goodbye!") # does not run ("dead code")

print(isPositive(5))  # prints Hello, then True

# No return statement returns None
def f(x):
    x + 42

print(f(5)) # None

# 3. Print versus Return

# This is a common early mistake (confusing print and return):
def cubed(x):
    print(x**3) # Here is the error!

cubed(2)          # seems to work!
print(cubed(3))   # sort of works (but prints None, which is weird)
print(2*cubed(4)) # Error!

# Correct implementation
def cubed(x):
    return (x**3) # That's better!

cubed(2)          # seems to be ignored (why?)
print(cubed(3))   # works!
print(2*cubed(4)) # works!

# 4. Different Parameter and Return Types
def hypotenuse(a, b):
    return ((a**2) + (b**2))**0.5

print(hypotenuse(3, 4)) # 5.0 (not 5)
print("---------------------")

def xor(b1, b2):
    return ((b1 and (not b2)) or (b2 and (not b1)))  # same as (b1 != b2)

print(xor(True,  True))  # False
print(xor(True,  False)) # True
print(xor(False, True))  # True
print(xor(False, False)) # False
print("---------------------")

def isPositive(n):
    return (n > 0)

print(isPositive(10))     # True
print(isPositive(-1.234)) # False

#8. Scope

# 8 - 1: Local Variable Scope

def f(x):
    print("In f, x =", x)
    x += 5
    return x

def g(x):
    return f(x*2) + f(x*3)

print(g(2))

def f(x):
    print("In f, x =", x)
    x += 7
    return round(x / 3)

def g(x):
    x *= 10
    return 2 * f(x)

def h(x):
    x += 3
    return f(x+4) + g(x)

print(h(f(1)))

# 8 - 2: Global Variable Scope

# In general, you should avoid using global variables.
# You will even lose style points if you use them!
# Still, you need to understand how they work, since others
# will use them, and there may also be some very few occasions
# where you should use them, too!

g = 100

def f(x):
    return x + g

print(f(5)) # 105
print(f(6)) # 106
print(g)    # 100

g = 100

def f(x):
    # If we modify a global variable, we must declare it as global.
    # Otherwise, Python will assume it is a local variable.
    global g
    g += 1
    return x + g

print(f(5)) # 106
print(f(6)) # 108
print(g)    # 102





