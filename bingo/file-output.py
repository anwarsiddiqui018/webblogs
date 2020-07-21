# f = open('hello_world.txt','a')
# f.write('\n' + 'hum honge kaamyab')
#
# f.close()


#
# f = open('hello_world.txt','r')
# message = f.read()
# print(message)
# f.close()


a = "anwar ahmed"
print(a.split())

# list comprehension

# mylist = []
# for i in "anxiety":

#     mylist.append(i)
# print(mylist)


i = [i*2 for i in {3,1,2}]
print(i)

remainder = lambda num: num % 2
print(remainder(5))

multiply = lambda x,y: x*y
print(multiply(2,3))

myset = {3,1,2}
makelist = lambda i: list(i)
mylist = makelist(myset)
print(mylist)
