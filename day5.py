# HW
"""
1. Basic for Loop
    Suppose you want to write a program that prints numbers from 1 to 10, formatted like this:
    Current value: 1
    Current value: 2
    ...
    Current value: 10

    How can you do that?

2. Basic while Loop
    Try the above exercise using a while loop. 
    You’ll need to define a counter and an appropriate stopping condition. 
    And you’ll need to manually increment the counter after every loop.

3. hasConsecutiveDigits(n)

4. rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2) 
"""

# Conditionals and Loops Review

# 1. Given the nested if-else structure below, what will be the value of x after code execution completes

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


# 2. What is the value of x

x = 0
while (x < 100):
  x+=2
print(x)


# 3. Given the nested if-else below, what will be the value x when the code executed successfully

x = 0
a = 5
b = 5
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


# 4. What is the output of the following for loop and  range() function

for num in range(-2,-5,-1):
    print(num, end=", ")

# 5. What is the output of the following range() function

for num in range(2,-5,-1):
    print(num, end=", ")

# 6. What is the output of the following if statement

a, b = 12, 5
if a + b > 17:
    print('Seventeen')
elif a - b >= 7:
    print('Seven')
else:
    print('None')

# 7. What is the output of the following loop

for l in 'Jhon':
   if l == 'o':
      continue
   print(l, end=", ")

# 8. What is the value of the var after the for loop completes its execution

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)


# Nested Loops!

"""
Nested loops mean loops inside a loop. For example, while loop inside the for loop, for loop inside the for loop, etc.
"""

for i in range(4):
    print(f'{i}: ')
    for j in range(10):
        if j < 9:
            print(i * 10 + j, end = ", ")
        else:
            print(i * 10 + j, end = " ")
    print()


# Python Nested Loop Syntax
"""
Outer_loop Expression:
    Inner_loop Expression:
        Statement inside inner_loop
    Statement inside Outer_loop
"""

# Example 1: Basic Example of Python Nested Loops

for i in range(1, 3):
    for j in range(4, 6):
	    print(i, j)

# Example 2: Printing multiplication table using Python nested for loops

# Running outer loop from 2 to 3
 
for i in range(2, 4):
 
    # Printing inside the outer loop
    # Running inner loop from 1 to 10
    for j in range(1, 11):
 
        # Printing inside the inner loop
        print(i, "*", j, "=", i*j)
    # Printing inside the outer loop
    print()

# Running outer loop from 2 to 3
for i in range(2, 4):
 
    # Printing inside the outer loop
    # Running inner loop from 1 to 10
    for j in range(1, 11):
      if i==j:
        break
      # Printing inside the inner loop
      print(i, "*", j, "=", i*j)
    # Printing inside the outer loop
    print()


# Running outer loop from 2 to 3
for i in range(2, 4):
 
    # Printing inside the outer loop
    # Running inner loop from 1 to 10
    for j in range(1, 11):
      if i==j:
        continue
      # Printing inside the inner loop
      print(i, "*", j, "=", i*j)
    # Printing inside the outer loop
    print()


""" ------------------------------------------------------------------------- """

# Strings

# 1. String Literals
# single-quoted or double-quoted strings are the most common
print('single-quotes')
print("double-quotes")

# triple-qouted strings are less common (though see next section for a typical use)
print('''triple single-quotes''')
print("""triple double-quotes""")

# 2. New Lines in Strings
print("abc\ndef")  # \n is a single newline character
print("""abc
def""")

print("""\
You can use a backslash at the end of a line in a string to exclude
the newline after it. This should almost never be used, but one good
use of it is in this example, at the start of a multi-line string, so
the whole string can be entered with the same indentation (none, that is).
""")

# 3. More Escape Sequences
print("Double-quote: \"")
print("Backslash: \\")
print("Newline (in brackets): [\n]")
print("Tab (in brackets): [\t]")

print("These items are tab-delimited, 3-per-line:")
print("abc\tdef\tg\nhi\tj\\\tk\n---")

# An escape sequence produces a single character:
s = "a\\b\"c\td"
print("s =", s)
print("len(s) =", len(s))




