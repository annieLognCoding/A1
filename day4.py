#Review

def isFactor(f, n):
    return False # replace with your solution

def testIsFactor():
    print("Testing isFactor()...", end="")
    assert(isFactor(2, 2))
    assert(isFactor(2, 4))
    assert(not isFactor(2, 5))
    assert(not isFactor(0, 6))
    assert(isFactor(6, 0))
    assert(isFactor(0, 0))
    assert(isFactor(-2, 4))
    print("Passed!")

# testIsFactor()

def kthDigit(n, k):
    return 42 # replace with your solution

def testKthDigit():
    print("Testing kthDigit()...", end="")
    assert(kthDigit(0,0) == 0)
    assert(kthDigit(789, 0) == 9)
    assert(kthDigit(789, 1) == 8)
    assert(kthDigit(789, 2) == 7)
    assert(kthDigit(789, 3) == 0)
    assert(kthDigit(-1234, 3) == 1)
    assert(kthDigit(-3, 1) == 0)
    print("Passed!")

# testKthDigit()

def eggCartons(eggs):
    return 42 # replace with your solution

def testEggCartons():
    print("Testing eggCartons()...", end="")
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print("Passed.")
    print("(Add more tests to be more sure!)")

# testEggCartons()

"""

Given a number n, return True if n is in the range 1..10, inclusive. 
Unless outside_mode is True, in which case return True if the number is less or equal to 1, 
or greater or equal to 10.

"""

def in1to10(n, outside_mode):
    return True


# 1. For loops

def sumFromMToN(m, n):
    total = 0
    # note that range(x, y) includes x but excludes y
    for x in range(m, n+1):
        total += x
    return total

print(sumFromMToN(5, 10) == 5+6+7+8+9+10)


#Take out the first parameter?
def sumToN(n):
    total = 0
    for x in range(n+1):
        total += x
    return total

print(sumToN(5) == 0+1+2+3+4+5)


#Add a third parameter?
def sumEveryKthFromMToN(m, n, k):
    total = 0
    for x in range(m, n+1, k):
        total += x
    return total

print(sumEveryKthFromMToN(5, 20, 7) == (5 + 12 + 19))

#Just odd numbers?
def sumOfOddsFromMToN(m, n):
    total = 0
    for x in range(m, n+1):
        if (x % 2 == 1):
            total += x
    return total

print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))


# Printing Stars
def printStars(n):
    for i in range(n):
        print("*" * (i+1))

printStars(5)
# 2. While loops

# use while loops when there is an indeterminate number of iterations

def getInput():
    gotInput = False
    while(not gotInput):
        x = input("Please Enter input: ")
        if(x):
            print("You entered: ", x)
            gotInput = True

getInput()


def leftmostDigit(n):
    n = abs(n)
    while (n >= 10):
        n = n//10
    return n

print(leftmostDigit(72658489290098) == 7)

# eg: find the nth number that is a multiple of either 4 or 7
def isMultipleOf4or7(x):
    return ((x % 4) == 0) or ((x % 7) == 0)

def nthMultipleOf4or7(n):
    found = 0
    guess = -1
    while (found <= n):
        guess += 1
        if (isMultipleOf4or7(guess)):
            found += 1
    return guess

print("Multiples of 4 or 7: ", end="")
for n in range(15):
    print(nthMultipleOf4or7(n), end=" ")
print()


def digitCount(n):
    return 42 # replace with your solution

def testDigitCount():
    print("Testing digitCount()...", end="")
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print("Passed!")

# testDigitCount()


def hasConsecutiveDigits(n):
    return 42 # replace with your solution

def testHasConsecutiveDigits():
    print("Testing hasConsecutiveDigits()...", end="")
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print("Passed!")

# testHasConsecutiveDigits()