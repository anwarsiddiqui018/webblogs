# def count_chars(city):
#
#     result = {}
#     city_in = city.lower()
#     for char in city_in:
#         if char == ' ':
#             pass
#         elif char in result:
#             result[char] += 1
#             # print('*')
#
#         else:
#             result[char] = 1
#
#     return result
# print(count_chars("CHICAGO Berlin"))

# def count_chars(city):
#     city = city.lower()
#     results = ""
#     for i in city:
#         if i in results:
#             pass
#         elif i == " ":
#             pass
#         else:
#             results += i + ":" + ("*" * city.count(i)) + ","
#
#     return results
# print(count_chars("CHICAGO Berlin"))


# def string_letter_count(s):
#     s_str = s.lower()
#     result = ""
#     for str in s_str:
#         if str == "":
#             return ""
#         elif str == "12":
#             return ""
#         else:
#             pass
#
#         #     return ""
#         # elif:
#         #     str += 1
#         #
#         # else:
#         #     str = 1
#     return str
#
#
# print(string_letter_count(""))

# def count_words(s):
#     d = ""
#     for i in s:
#         d = s.count(i)
#     return d
#
# print(count_words("CHICAGO"))












# def string_letter_count(s):
#     s = s.lower()
#     L1=[]
#     for i in s:
#         L1.append(i)
#     L1.sort()
#     s = "".join(L1)
#     A={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
#     L=[]
#     for i in s:
#         if i not in L:
#             if i in A:
#                 L.append(str(s.count(i)))
#                 L.append(str(i))
#     return "".join(L)






def string_letter_count(s):
    string = []
    s = s.lower()
    s = ''.join(sorted(s))
    for char in s:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            string.append(str(s.count(char)) + char + ",")
            s = s.replace(char, '')    # repeated characters will be removed
    s = ''
    for i in string:
        if '0' not in i:    # it is used to drop elements in the list
            s += i
    return s
print(string_letter_count("CHICAGO  wefwdwww1233"))