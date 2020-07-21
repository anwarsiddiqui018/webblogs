# ()  , _ ,

lst = [1,34,56,78,89,23]
sum1 = 0
for i in lst:
    sum1 += i
print(sum1)


### Get the largest number from a list

def largest_in_list(lst):
    lst.sort()
    lst1 = lst[-1]
    return lst1
print(largest_in_list([1,2,3,45]))


####        or

def largest_in_list(lst):
    max = lst[0]
    for a in lst:
        if a > max:
            max = a
    return max

print(largest_in_list([1,2,3,45]))



###  Remove duplicates from a list

def remove_duplicate(lst):
    unique_item = set()
    duplicate_item = []
    for x in lst:
        if x not in duplicate_item:
            duplicate_item.append(x)
            unique_item.add(x)
    return duplicate_item
print(remove_duplicate([1,233,4,44,4]))


def check_list(lst):
    # lst = []
    if not lst:
        return "list is empty"
    else:
        return lst

print(check_list([1,233,4,44,4]))
print(check_list([]))