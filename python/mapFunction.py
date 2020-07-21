def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


print("  ")
# print("\n")


sequence = ['a', 'n', 'w', 'a', 'r', 'a', 'h', 'm', 'e', 'd', 's', 'i', 'd', 'd', 'i', 'q', 'u', 'i']

filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)


def calculatesqure(n):
    return n * n


numbers = (1, 2, 3, 4, 5)
results = map(calculatesqure, numbers)
print(results)

# coverting map object to set

numberSquare = set(results)
print(numberSquare)

# use lambda function with map()

numbers = (1, 2, 3, 4, 5)
results1 = map(lambda x: x * x, numbers)
print(results1)

numberSquare1 = set(results1)
print(numberSquare)

# Passing Multiple Iterators to map() Using Lambda

num1 = [1, 2, 3]
num2 = [4, 5, 6]

sum = map(lambda n1, n2: n1 + n2, num1, num2)
print(list(sum))


def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'mango'))

print(list(x))





lst_even = []

old_list = [2, 1, 3, 8, 10, 11, 13]
list_if_even = list(filter(lambda x: x % 2 == 0, old_list))
# print(x)
# lst_even.append(list_if_even)
# print(lst_even)

list_if_odd = list(map(lambda x: x%2 != 0, old_list))

print(list_if_even)
print(list_if_odd)

print("Are any of the elements even? " + str(any(list_if_even)))
print("Are any of the elements odd? " + str(any(list_if_odd)))

# #Print Even numbers in a list using Lambda function
# my_list = [3,5,2,11,6,8]
# list_Even_Numbers = list(map(lambda varX: varX % 2 == 0,my_list))
# print("Following are Even numbers in the list ="+ str(list_Even_Numbers))
#
#
# #Print Odd numbers in a list using Lambda function
# my_list = [3,5,2,11,6,8]
# list_Odd_Numbers = list(map(lambda varX: varX % 2 == 1,my_list))
# print("Following are Odd numbers in the list ="+ str(list_Odd_Numbers))