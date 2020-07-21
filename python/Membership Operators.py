# # # ()  , _ ,
# #
# # # Python program to illustrate
# # # Finding common member in list
# # # using in operator
# #
# # list1 = [1,2,3,4,5]
# # list2 = [1,2,3,4,5] #[6.7,8,9]
# #
# # for i in list1:
# #     if i in list2:
# #         print("The list is overlapping")
# # else:
# #     print("The list is not overlapping")
# #
# #
#
#
#
# # Same example without using in operator:
# def overlapping(list1, list2):
#     count=0
#     d=0
#     for i in list1:
#         count += 1
#         print(count)
#     for i in list2:
#         d += 1
#
#     for i in range(0, count):
#         for j in range(0, d):
#             if(list1 == list2):
#                 return 1
#     return 0
# list1 = [9,65,67]
# list2 = [6.7,8,9]
#
# if(overlapping(list1, list2)):
#     print("overlapping")
# else:
#     print("not overlapping")
#
#
# import random
#
# lis3 = [9,65,67]
# random.shuffle(lis3)
# print(lis3)
#
#
# lst4 = ['a', 'n', 'w', 'a', 'r']
# lst5 = ['a','h','m','e','d']
# a1 = lst4.append('a')
# print(lst4+lst5)
# a = ''.join(lst4)  # join method provides a flexible way to ceate a string from iterable objects
# # a= ''.join(ls)
# print(a)
#
#
def count_char_freq(str1):
    all_freq = {}
    for char in str1:
        keys = all_freq.keys()
        if char in keys:
            all_freq[char] += 1
        else:
            all_freq[char] = 1
    return all_freq
print(count_char_freq("My name is khan"))






