f = open("drmofile.txt", "r")
# print(f.read())

data = f.read()

words = data.split()

print('Number of words in text file :', len(words))






