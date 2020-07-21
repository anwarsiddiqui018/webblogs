#  ()   _
def sum_list(list):
    sum = 1
    for i in list:
        sum = sum * i
    return sum
print(sum_list([1,2,3]))





def even_num(lst):
    even_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
print(even_num([1,2,3,4,5,6,7,8,9]))


def perfect_num(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return "Perfect number"
    else:
        return "Not a Perfect number"
print(perfect_num(28))