# # Hw
# # We have a loud talking parrot. The "hour" parameter is the current hour time in the
# # range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after
# # 20. Return True if we are in trouble.
import random

# # Example Execution:
# # parrot_trouble(True, 6) → True
# # parrot_trouble(True, 7) → False
# # parrot_trouble(False, 6) → False
# # Starter Code (you can copy this code to your VSCode and change the function
# # definition):

# def parrot_troube(talking, hour):
#     if(hour < 7 or hour > 20 and talking):
#         return True
#     return False


# # Given 2 int values, return True if one is negative and one is positive. Except if the
# # parameter "negative" is True, then return True only if both are negative.
# # Example Execution:
# # pos_neg(1, -1, False) → True
# # pos_neg(-1, 1, False) → True
# # pos_neg(-4, -5, True) → True
# # Starter Code:
# # def pos_neg(num1, num2, negative):
# # return False


# def pos_neg(num1, num2, negative):
#     if(negative == True):   
#         return (num1 < 0 and num2 < 0)
#     else:
#         return (num1 > 0 and num2 < 0) or (num1 < 0 and num2 > 0)
    

# def date_fashion(you, date):
#     if(you > 8 or date > 8):
#         return 2
#     if(you <= 2 or date <= 2):
#         return 0
#     return 1

# def caught_speeding(speed, is_birthday):
#     if(is_birthday):
#         speed -= 5
#     if(speed > 60 and speed <= 80):
#         return 1
#     if(speed > 81):
#         return 2
#     return 0

# print(caught_speeding(60, False))
# print(caught_speeding(65, False))
# print(caught_speeding(65, True))
# print(caught_speeding(92, True))

    

# #Review

# # % --> remainder

# def isFactor(f, n):
#     if(f % n == 0):
#         return True
#     return False # replace with your solution

# def testIsFactor():
#     print("Testing isFactor()...", end="")
#     assert(isFactor(2, 2))
#     assert(isFactor(2, 4))
#     assert(not isFactor(2, 5))
#     assert(not isFactor(5, 6))
#     assert(isFactor(6, 12))
#     assert(isFactor(-2, 4))
#     print("Passed!")

# # testIsFactor()

# def kthDigit(n, k):
#     return 42 # replace with your solution

# def testKthDigit():
#     print("Testing kthDigit()...", end="")
#     assert(kthDigit(0,0) == 0)
#     assert(kthDigit(789, 0) == 9)
#     assert(kthDigit(789, 1) == 8)
#     assert(kthDigit(789, 2) == 7)
#     assert(kthDigit(789, 3) == 0)
#     assert(kthDigit(-1234, 3) == 1)
#     assert(kthDigit(-3, 1) == 0)
#     print("Passed!")

# # testKthDigit()

# # % and //
# def eggCartons(eggs):
#     cartons = (eggs + 11) // 12
#     return cartons # replace with your solution

# def testEggCartons():
#     print("Testing eggCartons()...", end="")
#     assert(eggCartons(0) == 0)
#     assert(eggCartons(1) == 1)
#     assert(eggCartons(12) == 1)
#     assert(eggCartons(13) == 2)
#     assert(eggCartons(24) == 2)
#     assert(eggCartons(25) == 3)
#     print("Passed.")
#     print("(Add more tests to be more sure!)")

# # testEggCartons()

# # Given two int values, a and b, return True if either one is 6. Or if their sum or
# # difference is 6. Otherwise return False
# # Example Execution:
# # love6(6, 4) → True
# # love6(4, 5) → False
# # love6(1, 5) → True
# # love6(8, 14) -> True

# # Starter Code:

# def love6(a, b):
#     if(a + b == 6): return True 
#     if(a == 6 or b == 6): return True 
#     if(abs(a - b) == 6): return True 

#     return False #replace with your code


# def love6_vB(a, b):
#     return (a == 6 or b == 6) or (a + b == 6) or (abs(a-b) == 6) #replace with your code


# """

# Given a number n, return True if n is in the range 1..10, inclusive. 
# Unless outside_mode is True, in which case return True if the number is less or equal to 1, 
# or greater or equal to 10.

# """

# def in1to10(n, outside_mode):
#     return True


# 1. For loops

# for i in range(1, 11):
#     print("hi, " + str(i))



# def sumFromMToN(m, n):
#     total = 0
#     # note that range(x, y) includes x but excludes y
#     for x in range(m, n+1):
#         total += x
#     return total

# print(sumFromMToN(2, 5))

# print(sumFromMToN(5, 10) == 5+6+7+8+9+10)


# #Take out the first parameter?
# def sumToN(n):
#     total = 0
#     for x in range(n+1):
#         total += x
#     return total

# print(sumToN(5) == 0+1+2+3+4+5)


#Add a third parameter?
def sumEveryKthFromMToN(m, n, k):
    total = 0
    for x in range(m, n+1, k): #5, 12, 19
        total += x
    return total

# print(sumEveryKthFromMToN(5, 20, 7))


# print(sumEveryKthFromMToN(5, 20, 7) == (5 + 12 + 19))

# #Just odd numbers?
# def sumOfOddsFromMToN(m, n):
#     total = 0
#     for x in range(m, n+1):
#         if (x % 2 == 1):
#             total += x
#     return total

# print(sumOfOddsFromMToN(4, 10) == sumOfOddsFromMToN(5,9) == (5+7+9))

# Printing Stars
# def printStars(n):
#     for i in range(n, n+6): #i = 0, 1, 2, .... , n-1
#         print("*" * (i))

# printStars(5)


# def printX(n, m):
#     if (n % 2 != 0): n += 1 #if n is odd, make it the next even number
#     if (m % 2 == 0): m += 1 #if m is even, make it the next odd number
#     for i in range(n, m, 2): #i = 4, 12; 4, 6, 8, 10, 12
#         print("x" * (i // 2))

# # 2. While loops

# use while loops when there is an indeterminate number of iterations

def getInput():
    gotInput = False
    while(not gotInput):
        x = input("Please Enter input: ")
        if(x):
            print("You entered: ", x)
            gotInput = True

# getInput()


# def guessNumber():
#     num = int(random.random() * 100) + 1
#     guess = -1
#     while(guess != num): 
#         guess = int(input("Guess a number: "))
#         if(guess > num):
#             print("guess is too big")
#         if(guess < num):
#             print("guess is too small")

# def printStar():
#     num = input("Enter a number: ")
#     while(num != "stop"):
#         print("*" * int(num))
#         num = input("Enter a number: ")

# printStar()


#define a function that takes in a number from the terminal
#prints out that many stars
#keep running the function until user inputs "stop"

def leftmostDigit(n):
    n = abs(n)
    while (n >= 10):
        n = n//10
    return n

print(leftmostDigit(22335), leftmostDigit(122335), leftmostDigit(32335))

# print(leftmostDigit(72658489290098) == 7)

# # eg: find the nth number that is a multiple of either 4 or 7
# def isMultipleOf4or7(x):
#     return ((x % 4) == 0) or ((x % 7) == 0)

# def nthMultipleOf4or7(n):
#     found = 0
#     guess = -1
#     while (found <= n):
#         guess += 1
#         if (isMultipleOf4or7(guess)):
#             found += 1
#     return guess

# print("Multiples of 4 or 7: ", end="")
# for n in range(15):
#     print(nthMultipleOf4or7(n), end=" ")
# print()


def digitCount(n):
    n = abs(n)
    count = 1
    while(n // 10 > 0):
        count += 1
        n = n // 10

    return count # replace with your solution

# print(digitCount(333))

def testDigitCount():
    print("Testing digitCount()...", end="")
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print("Passed!")

testDigitCount()


# def hasConsecutiveDigits(n):
#     return 42 # replace with your solution

# def testHasConsecutiveDigits():
#     print("Testing hasConsecutiveDigits()...", end="")
#     assert(hasConsecutiveDigits(0) == False)
#     assert(hasConsecutiveDigits(123456789) == False)
#     assert(hasConsecutiveDigits(1212) == False)
#     assert(hasConsecutiveDigits(1212111212) == True)
#     assert(hasConsecutiveDigits(33) == True)
#     assert(hasConsecutiveDigits(-1212111212) == True)
#     print("Passed!")

# # testHasConsecutiveDigits()