import math

def is_square(n):
    print(n)

    root = math.sqrt(n)
    print(root)

    if n == int(root + 0.5) ** 2:
        root = math.sqrt(n) + 1
        print(root)
        return root*root
    else:
        return -1  # fix me

print(is_square(121))
