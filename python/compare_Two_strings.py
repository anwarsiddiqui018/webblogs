# Compare two strings by comparing the sum of their values (ASCII character code).
#
# For comparing treat all letters as UpperCase
# null/NULL/Nil/None should be treated as empty strings
# If the string contains other characters than letters, treat the whole string as it would be empty
# Your method should return true, if the strings are equal and false if they are not equal.
# ()  , _ ,


def string_cnt(s):
    try:
        if s.isalpha():
            return sum(ord(a) for a in s.upper())
    except AttributeError:
        pass



def compare(s1, s2):
    return string_cnt(s1) == string_cnt(s2)

s1 = 'AD'
s2 = 'BC'

print(compare("AD", "BC"))
