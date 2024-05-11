# HW REVIEW!
# Quick Review:
"""
1. When you for loop through a string, you can access all of its characters.
    Ex:
    for c in "annie": c = a, n, n, i, e
        print(c)
    Output:
    a
    n
    n
    i
    e
"""
"""
2. You can access a character in a string with the character index. 
The character index starts as 0 and ends at string length - 1.

    Ex: "annie"[2] == "n", "annie"[4] == "e"
"""

"""
3. You can access length of string with the len method.
    Ex: len("annie") == 5
"""

"""
Define a function double_char that takes in a string and returns a new string where
for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
double_char('AND') => 'AANNDD'

"""
def double_char(str):
    result = ""
    for c in str:
        result += c + c
    return result

double_char('The')
double_char('AAbb')
double_char('Hi-There')


"""
2. Return the number of times that the string "hi" appears anywhere in the
    given string.

    count_hi('abc hi ho') → 1
    count_hi('ABChi hi') → 2
    count_hi('hihi') → 2
    count_hi('hihellohihi') -> 3
"""

def count_hi(str):
    # "hi" is the first substring of str?
    count = 0
    for i in range(0, len(str) - 1): #i = 0, 1, ... len(str) - 1
        if(str[i] == "h" and str[i+1] == "i"):
            count += 1
    return count



# print(count_hi('abc hi ho'))
# print(count_hi('ABChi hi'))
# print(count_hi('hihi'))
# print(count_hi('hihellohihi'))

"""
Define a function that takes in a string and returns True if the string "cat"
and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

"""
 
 
def cat_dog(str):
    countCat = 0
    countDog = 0
    for i in range(0, len(str) - 2):
        if(str[i] == "c" and str[i + 1] == "a" and str[i + 2] == "t"):
            countCat += 1
        if(str[i] == "d" and str[i + 1] == "o" and str[i + 2] == "g"):
            countDog += 1
    return countCat == countDog

"""
Define a function that takes in a string and returns the number of times
that the string "co*e" appears anywhere in the given string; we'll accept
any letter for the '*', like “code”, “cope”, “cooe”, etc.
    count_code('aaacodebbb') → 1
    count_code('codexxcode') → 2
    count_code('cozexxcope') → 2
"""

"""
Define a function that takes in two strings, and returns True if either of the
strings appears at the very end of the other string, ignoring upper/lower
case differences (in other words, the computation should not be "case
sensitive"). 

Note: s.lower() returns the lowercase version of a string.
    end_other('Hiabc', 'abc') → True
    end_other('AbC', 'HiaBc') → True
    end_other('abc', 'abXabc') → True
"""

def end_other(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    # return whether 
    # str1 appears at the end of str2 
    # or str2 appears at the end of str1
        # len(str1), len(str2) gives us the string length

    if(len(str1) > len(str2)):
        bigger_string = str1
        smaller_string = str2
    else:
        bigger_string = str2
        smaller_string = str1
    
    for i in range(0, len(smaller_string)):
        if (bigger_string[len(bigger_string) - (len(smaller_string) - i)] != smaller_string[i]):
            return False
    
    return True


"""
Define a function that takes in a string and returns true if the given string
contains an appearance of "xyz" where the xyz is not directly preceded by
a period (.). So "xxyz" counts but "x.xyz" does not.

    xyz_there('abcxyz') → True
    xyz_there('abc.xyz') → False
    xyz_there('xyz.abc') → True

    2:31 --> turn in an answer to annie.chang@logncoding.com
"""

def xyz_there(str):
    # go through the string as we did before and check if str[i], str[i + 1], str[i + 2] == 'x', 'y', 'z'
        # but do one extra check afterwards --> was str[i-1] == '.' ?
    for i in range(0, len(str) - 2):
        if str[i] == 'x' and str[i + 1] == 'y' and str[i + 2] == 'z':
            if i > 0 and str[i - 1] != '.' or i == 0:
                return True
    return False

# print(xyz_there('abc.xyz')) 
# print(xyz_there('xyz.abc'))
# print(xyz_there('abcxyz'))

"""
Some String Operators
"""

# # 1. String + and *
# print("abc" + "def")
# print("abc" * 3)

# 2. The in operator
# print("ring" in "strings")
# print("wow" in "amazing!")
# print("Yes" in "yes!")
# print("" in "No way!")
# print("no" in "snow")
# print("hyung" in "Hyungjoon")

# String indexing and slicing

s = "abcdefgh"
# print(s[1:len(s):2])
# print(s[0:5:3])
print(s[::-1])