# # # ()  , _ ,
### second smallest number
print("second smallest")
def second_smallest_num(lst):
    if (len(lst) < 2):
        return
    if( (len(lst) == 2) and (lst[0] == lst[1]) ):
        return
    dup_items = set()
    # print(dup_items)
    unique_items = []
    for x in lst:
        if x not in dup_items:
            unique_items.append(x)
            dup_items.add(x)
    unique_items.sort()
    return unique_items[1]
print(second_smallest_num([1, 2, -8, -2, 0, -2]))
print(second_smallest_num([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest_num([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest_num([2,2]))
print(second_smallest_num([2]))
print("\n")

### second largest
print("second largest\n")

def second_largest(lst):
    if (len(lst) < 2):
        return
    if((len(lst) == 2) and (lst[0] == lst[1])):
        return
    duplicate_items= set()
    unique_items = []
    for x in lst:
        if x not in duplicate_items:
            unique_items.append(x)
            duplicate_items.add(x)
    unique_items.sort()
    return unique_items[-2]
print(second_largest([1,2,3,4,4,4,6,9,]))
print(second_largest([1,2]))
print(second_largest([2,2]))
print(second_largest([1,2,3,4,4]))
print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_largest([2,2]))
print(second_largest([1]))

print("\n")
# Get unique values from a list
print("Get unique values from a list")

my_list = [1, 1, 1, 0, 0, 0, 2, -2, -2]
print("Original list: ", my_list)
my_set = set(my_list)
a = my_set.add(10)
print(my_set)
print("\n")






# covert list into dictionary
print("covert list into dictionary")

colourName = ['Black', 'Red', 'Maroon', 'Yellow']
colourCode = ['#000000', '#FF0000', '#800000', '#FFFF00']
for key, value in zip(colourName,colourCode):

    print([{'colourName': key, 'colourCode': value} ] )