# def to_jaden_case(string):
#     words = []
#     st = string.split()
#     print(st)
#     for i in st:
#         il = list(i)
#         print(il)
#         il[0] = il[0].upper()
#         words.append(''.join(il))
#         # print(words)
#     return ' '.join(words)
# print(to_jaden_case("how caaren't real"))









def fun(a, **kwargs):
    print("a is", a)
    print("We expect kwargs 'b' and 'c' in this function")
    print("b is", kwargs['b'])
    print("c is", kwargs['c'])


fun(1, b=4, c=5)