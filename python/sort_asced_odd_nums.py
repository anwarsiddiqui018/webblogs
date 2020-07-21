# def sort_array(soure_array):
#     arr = []
#     val = soure_array.split()
#
#     for i in val:
#         il = list(i)
#         if il % 2 == 0:
#             pass
#         else:
#             arr.append(''.join(il))
#     return ' '.join(arr)
#
#
#
#
# sort_array([1,2,3,4,5])
# print(sort_array())


#
# import numpy as np
#
# def selection_sort(x):
#     for i in range(len(x)):
#         if i % 2 != 0:
#             pass
#
#         else:
#
#             swap = i + np.argmin(x[i:])
#             (x[i], x[swap]) = (x[swap], x[i])
#         return x
#
# # x = np.array()
# # selection_sort(x)
# print(selection_sort([5, 3, 1, 8, 0]))


def sort_array(source_array):
    odd_numbers = sorted([n for n in source_array if n%2!=0])
    c = 0
    res = []
    for i in source_array:
        if i % 2!=0:
            res.append(odd_numbers[c])
            print(res)
            c = c + 1
            print(c)
        else:
            res.append(i)
    return res

print(sort_array([23, 3, 12, 8, 0]))

