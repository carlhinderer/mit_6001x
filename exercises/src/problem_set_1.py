# Problem 1
# Assume s is a string of lower case characters.
#
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5


def count_vowels(s):
    vowel_count = 0
    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
    return vowel_count


def test_count_vowels_interactively():
    s = input('Enter a string: ')
    print('Number of vowels:', count_vowels(s))


# Problem 2
# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if
#   s = 'azcbobobegghakl', then your program should print:
# Number of times bob occurs is: 2


def count_bobs(s):
    bob_count = 0
    for i in range(len(s) - 2):
        if s[i:i + 3] == 'bob':
            bob_count += 1
    return bob_count


def test_count_bobs_interactively():
    s = input('Enter a string: ')
    print('Number of times bob occurs is:', count_bobs(s))


# Problem 3
# Assume s is a string of lower case characters.
#
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh
#
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should
#   print:
# Longest substring in alphabetical order is: abc


def longest_alphabetic_substr(s):
    longest, current = '', ''
    for c in s:
        if current == '' or c >= current[-1]:
            current += c
        else:
            if len(current) > len(longest):
                longest = current
            current = ''
    if len(current) > len(longest):
        longest = current
    return longest


def test_longest_alphabetic_interactively():
    print('not implemented')
