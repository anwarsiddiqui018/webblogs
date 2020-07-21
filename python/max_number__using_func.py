#  ()   _
def max_num(a,b,c):

    if (a > b) and (a > c):
        largest =  a
    elif (b > a) and (b > c):
        return b
    elif (c > a) and (c > b):
        return c
    else:
        return
print(max_num(5,6,7))


def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


# Driven code
a = 10
b = 14
c = 12
print(maximum(a, b, c))