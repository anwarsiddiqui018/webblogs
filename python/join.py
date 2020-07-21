# list1 = ['1','2','3','4']
# list2 = ['5']
# s = "-"
#
# # joins elements of list1 by '-'
# # and stores in sting s
# s = s.join(dir,list1)
#
# # join use to join a list of
# # strings to a separator s
# print(s)


# .join() with lists
# numList = ['1', '2', '3', '4']
# separator = ', '
# print(separator.join(numList))

# names = ['Java', 'Python']
# delimiter = ','
# single_str = delimiter.join(names)
# print('String: {0}'.format(single_str))


message ="Hello"

print(message,''.join('World')) #prints 'Hello World'


vowells = ["a", "e", "i", "o", "u"]
vowels_csv = ','.join(vowells)
print("vowels are", vowels_csv)


# names = 'Python'
# delimiter = ','
# single_str = delimiter.join(names)
# print('String: {0}'.format(single_str))
#
# indices_to_replace = [i for i, x in enumerate(file2) if x == 'fo12JUN2020bhav.csv']
#             for i in indices_to_replace:
#                 file2[i] = 'fob\\fobINDF'
# file2 = filename.split("\\")
            # name1 = file2[-1]
            # print(name1)
            # print(type(name1))


            # name = "\\".join(file2)



def split(word):
    return [char for char in word]

word = 'amwar'
print(split(word))