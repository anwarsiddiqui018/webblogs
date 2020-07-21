s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))


print("\t######")
#
#
#
# str = "Antarctica is cold"
#
# print('str = ', str)
# print('str[0] = ', str[0])
#
#
# arr = ['anw', 'ahm', 'sidd']
# print(arr)
# print(type(arr))
# arr1  = ('\\'.join(arr))
# print(arr1)
# print(type(arr1))
#
#
# text = 'Love their neighbour'
# print(text)
# i = text.split()
# print('\\'.join(i))
#
# grocery = 'Milk, Chicken, Bread, Butter'
#
# # maxsplit: 2
# p = (grocery.split(', ', 2))
# print('\\'.join(p))

# print("Hello {}, your balance is {:f}".format('Adam', 234.234))
# print("bin: {0:b}, oct: {0:o}, hex{0: x}".format(12))


song = 'cold, cold heart'
print(song.replace('cold', 'heart',1))




