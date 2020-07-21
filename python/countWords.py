# # Using list
def countString(s):
    string = []
    s = s.lower()
    # s = ''.join(sorted(s))
    for char in s:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            string.append(str(s.count(char)) + char + ", ")
    #         s = s.replace(char, '')
    # s = ''
    # for i in sorted(string, reverse=True):
    #
    #     if '0' not in i:
    #         s += i
    return s
print(countString("Anwar Ahmed Siddiqui"))
print("\n\n")

# def char_frequency(str):
#     dict = {}
#     for char in str:
#         keys = dict.keys()
#         if char in keys:
#             dict[char] += 1
#         else:
#             dict[char] = 1
#
#     return dict
# print(char_frequency("Anwar Ahmed Siddiqui 123"))

# Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with 'ing'
# then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.


def str_insert(str1):
    length = len(str1)

    if length > 2:
        if str1[-3:] == 'ing':
            str1 = str1 + 'ly'
        else:
            str1 = str1 + 'ing'

    return str1

print(str_insert('Anwar'))
print(str_insert('xyzpqe'))
print(str_insert('string'))
print(str_insert('me'))




# ()  , _ ,

def find_longest_word(words):
    word_len =[]

    for word in words:
        word_len.append((len(word), word))
        # print(word)

    word_len.sort(reverse=False)
    # i = word_len[-1][1]
    # # word_len[i] = 'khan'
    # words = words.replace(word_len[-1][1], 'Khan')
    print(words)


    return word_len[-1][1]



print(find_longest_word(['Anwar', 'Ahmed', 'Siddiqui', 'AliAhmed']))
# print(find_longest_word())






# def main():
#     text = input("Enter a list of words: ")
#     longest = 0
#
#     for word in text.split():
#
#         if len(word) > longest:
#             longest = len(word)
#             longest_word = word
#
#     print("longest word is ", longest_word, "with", len(longest_word))
#
#
# main()




# _

# def count_words(string1):
#     dict = {}
#     string1 = string1.lower()
#     for char in string1:
#         keys = dict.keys()
#         if char is ' ':
#             pass
#         elif char in keys:
#             dict[char] += 1
#         else:
#             dict[char] = 1
#
#     return dict
# print(count_words('My name is khan'))


