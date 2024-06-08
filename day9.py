import random

# str1 = 'jeehoon'
# print(str1[4], str1[1:6], str1[0:7], str1[:], str1[:3], str1[2:], str1[::3], str1[-3], str1[6:3:-1])
# #o eehoo jeehoon jeehoon jee ehoon jhn o noo 

# list1 = [1, 2, 3, 4, 5, 6, 7]
# print(list1[3], list1[1:6], list1[0:7], list1[:], list1[:3], list1[2:], list1[::3], list1[-3], list1[6:3:-1])
# 4 [2, 3, 4, 5, 6] [1, 2, 3, 4, 5, 6, 7] [1, 2, 3, 4, 5, 6, 7] [1, 2, 3] [3, 4, 5, 6, 7] [1, 4, 7] 5 [7, 6, 5]


# 1. Reverse a String
    # Write a Python program to reverse a given string using a loop.
def reverse_string(s):
    length = len(s)
    result = ''
    for i in range(-1, -1 * length - 1, -1):
        result += s[i]
    return result

# print(reverse_string('abcdefghijklmnopqrstuvwxyz'))

def reverse_string_2(s):
    return s[::-1]

# print(reverse_string_2('abcdefghijklmnopqrstuvwxyz'))


# 2. Sum of Elements in a List
    # Write a Python program to find the sum of all elements in a list of integers.
    # len(lst) --> gives you the length of the list

def sum_of_elements(lst):
    result = 0
    for i in range(0, len(lst)): #i = 0, 1, 2, 3, ..., len(lst) - 1
        result += lst[i]
    return result

# print(sum_of_elements([1, 2, 3, 4, 5]))


# 3. Count Vowels in a String
    # Write a Python program to count the number of vowels in a given string.
def count_vowels(s):
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
    return count

# print(count_vowels('Write a Python program to count the number of vowels in a given string.'))

"""
Cheat Sheet

1. Iterate through a list
"""
# for fruit in fruits:
#     print(fruit)

words = ['cat', 'dog', 'bird']
# for word in words:
#     print(word)

nums = [1, 2, 3, 4, 5, 6]
# for number in nums:
#     print(number)

"""
2. Iterate through a string
"""

name = 'Python'
# for char in name:
#     print(char)


"""
3. Iterate with indices
"""
# fruits = ['apple', 'banana', 'cherry']
# for i in range(len(fruits)):
#     print(fruits[i])


# 4. Find the Largest Element in a List
    # Write a Python program to find the largest element in a list of integers.
def largest_element(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

random_ints = []
for i in range(50):
    random_ints.append(int(random.random() * 100)  + 1)

# print(random_ints, largest_element(random_ints))


# 5. Remove Duplicates from a List
# Write a Python program to remove duplicate elements from a list of integers.

random_ints.remove(random_ints[33])

def remove_duplicates(lst):
    seen = []
    i = 0
    while i < len(lst):
        if not (lst[i] in seen):
            seen.append(lst[i])
        else:
            lst.remove(lst[i])
            i -= 1
        i += 1
    return lst

random_ints = []
for ind in range(10):
    num = int(random.random() * 100) + 1
    repeat = int(random.random() * 5) + 1
    random_ints.extend([num] * repeat)

# print(random_ints)

# print(remove_duplicates(random_ints))


# 6. Check for Palindrome
# Write a Python program to check if a given string is a palindrome.

def is_palindrome(s):
    for i in range(len(s) // 2):
        if(s[i] != s[-1 * (i+1)]):
            return False

    return True

print(is_palindrome('abbba'))

# 7. Find the Longest Substring Without Repeating Characters Write a Python program to find the longest substring without repeating characters in a given string.

"""
1. current substring
2. longest substring

>> if we find a repeated character within current substring, then stop
"""

def longest_substring_without_repeating(s):
    current_substring = ''
    longest_substring = ''
    for c in s:
        if c in current_substring:
            if(len(current_substring) > len(longest_substring)):
                longest_substring = current_substring
            current_substring = ''
        else:
            current_substring += c
    return longest_substring

print(longest_substring_without_repeating('Find the Longest Substring Without Repeating Characters Write a Python program to find the longest substring without repeating characters in a given string.'.replace(' ', '')))

"""
Rotate a List
Write a Python program to rotate a list of integers by a given number of positions.
def rotate_list(lst, k):
return None

Find the First Non-Repeating Character in a String
Write a Python program to find the first non-repeating character in a given string.
def first_non_repeating_character(s):
return None

Generate All Permutations of a String
Write a Python program to generate all permutations of a given string.
def generate_permutations(s, perm=""):
return None
"""

