class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Anwar', 'Siddiqui' , 50000)
emp_2 = Employee('test', 'user', 60000)

print(emp_1.email)
print(emp_2.email)

# emp_1.first = 'Anwar'
# emp_1.last = 'Siddiqui'
# emp_1.email = 'siddiqui.anwar018@gmail.com'
# emp_1.pay = 50000
#
# emp_2.first = 'test'
# emp_2.last = 'user'
# emp_2.email = 'test.user@gmail.com'
# emp_2.pay = 60000
#
print(emp_1.fullname())
print(emp_2.fullname())
# print('{} {}' .format(emp_1.first, emp_1.last))