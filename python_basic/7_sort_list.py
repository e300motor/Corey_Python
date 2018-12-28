li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li, reverse=True)

print('Sorted list = ', s_li)
print('Unsorted list = ', li)

li.sort(reverse=True)
print('Sorted list = ', li)
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

s_tup = sorted(tup)
print('Sorted tuple', s_tup)

di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Win'}

s_di = sorted(di)
print('Dict : ', s_di)

li2 = [-6, -5, -2, 3, 4]

s_li2 = sorted(li2, key=abs)
print(s_li2)


class Employee:

    def __init__(self, name, age, pay):  # first and self.first  : 'first' must be the same.
        self.name = name
        self.age = age
        self.pay = pay

    def __repr__(self):
        return '{} {} : {}'.format(self.name, self.age, self.pay)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 60000)
e3 = Employee('John', 39, 75000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_e = sorted(employees, key=e_sort)
s_e2 = sorted(employees, key=lambda e: e.name)
s_e3 = sorted(employees, key=lambda e: e.age)
print(s_e)
print(s_e2)
print(s_e3)
