"""
String Literals
"""
# 1. Four kinds of quotes
# single-quoted or double-quoted strings are the most common
print('single-quotes')
print("double-quotes")

# 2. New lines in strings
print("abc\ndef")  # \n is a single newline character

# 3. More Escape Sequences
print("Double-quote: \"")
print("Backslash: \\")
print("Newline (in brackets): [\n]")
print("Tab (in brackets): [\t]")

print("These items are tab-delimited, 3-per-line:")
print("abc\tdef\tg\nhi\tj\\\tk\n---")

# 4. Concatenated Literals
s = "abc" "def"
print(s)
# s = s "def" 

"""
Some String Operators
"""

# 1. String + and *
print("abc" + "def")
print("abc" * 3)
print("abc" + 3)  # error

# 2. The in operator
print("ring" in "strings")
print("wow" in "amazing!")
print("Yes" in "yes!")
print("" in "No way!")

# 3. String indexing and slicing

### Indexing a single character
s = "abcdefgh"
print(s)
print(s[0])
print(s[1])
print(s[2])

print("-----------")
print(s[len(s)-1])
print(s[len(s)])  # crashes (string index out of range)

### Negative indexes
s = "abcdefgh"
print(s)
print(s[-1])
print(s[-2])

### Slicing a range of characters
s = "abcdefgh"
print(s)
print(s[0:3])
print(s[1:3])
print("-----------")
print(s[2:3])
print(s[3:3])

### Slicing with default parameters
s = "abcdefgh"
print(s)
print(s[3:])
print(s[:3])
print(s[:])

### Slicing with a step parameter
print("This is not as common, but perfectly ok.")
s = "abcdefgh"
print(s)
print(s[1:7:2])
print(s[1:7:3])

### Reversing a string
s = "abcdefgh"

print("This works, but is confusing:")
print(s[::-1])

print("This also works, but is still confusing:")
print("".join(reversed(s)))

print("Best way: write your own reverseString() function:")

def reverseString(s):
    return s[::-1]

print(reverseString(s)) # crystal clear!

# 4. string split
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)

"""
Looping over Strings
"""

# 1. "for" loop with indexes
s = "abcd"
for i in range(len(s)):
    print(i, s[i])

# 2. "for" loop without indexes
s = "abcd"
for c in s:
    print(c)

#3. "for" loop with split
names = "fred,wilma,betty,barney"
for name in names.split(","):
    print(name)

"""
Example: isPalindrome
"""
# There are many ways to write isPalindrome(s)
# Here are several.  Which way is best?

def reverseString(s):
    return s[::-1]

def isPalindrome1(s):
    return (s == reverseString(s))

def isPalindrome2(s):
    for i in range(len(s)):
        if (s[i] != s[len(s)-1-i]):
            return False
    return True

def isPalindrome3(s):
    for i in range(len(s)):
        if (s[i] != s[-1-i]):
            return False
    return True

def isPalindrome4(s):
    while (len(s) > 1):
        if (s[0] != s[-1]):
            return False
        s = s[1:-1]
    return True

print(isPalindrome1("abcba"), isPalindrome1("abca"))
print(isPalindrome2("abcba"), isPalindrome2("abca"))
print(isPalindrome3("abcba"), isPalindrome3("abca"))
print(isPalindrome4("abcba"), isPalindrome4("abca"))

"""
Some String Methods
"""

# 1. Character types

# Run this code to see a table of isX() behaviors
def p(test):
    print("True     " if test else "False    ", end="")
def printRow(s):
    print(" " + s + "  ", end="")
    p(s.isalnum())
    p(s.isalpha())
    p(s.isdigit())
    p(s.islower())
    p(s.isspace())
    p(s.isupper())
    print()
def printTable():
    print("  s   isalnum  isalpha  isdigit  islower  isspace  isupper")
    for s in "ABCD,ABcd,abcd,ab12,1234,    ,AB?!".split(","):
        printRow(s)
printTable()

# 2. String edits

print("This is nice. Yes!".lower())
print("So is this? Sure!!".upper())
print("   Strip removes leading and trailing whitespace only    ".strip())
print("This is nice.  Really nice.".replace("nice", "sweet"))
print("This is nice.  Really nice.".replace("nice", "sweet", 1)) # count = 1

print("----------------")
s = "This is so so fun!"
t = s.replace("so ", "")
print(t)
print(s) # note that s is unmodified (strings are immutable!)

# 3. Substring search

print("This is a history test".count("is")) # 3
print("This IS a history test".count("is")) # 2
print("-------")
print("Dogs and cats!".startswith("Do"))    # True
print("Dogs and cats!".startswith("Don't")) # False
print("-------")
print("Dogs and cats!".endswith("!"))       # True
print("Dogs and cats!".endswith("rats!"))   # False
print("-------")
print("Dogs and cats!".find("and"))         # 5
print("Dogs and cats!".find("or"))          # -1
print("-------")
print("Dogs and cats!".index("and"))        # 5
print("Dogs and cats!".index("or"))         # crash!

"""Python String Formatting

To use formatted string literals, 
begin a string with f before the opening quotation mark.
Inside this string, you can write a Python expression between 
{ and } characters that can refer to variables or literal values.
"""

year = 2016
event = 'Referendum'
f'Results of the {year} {event}'

