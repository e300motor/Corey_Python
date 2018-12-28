
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

student['tall'] = 177
print(student['name'])          #if no 'name'  , raise exception
print(student.get('name'))    #if no 'name' , show 'Not Found'
print(student.get('phone', 'Not Found'))


student.update({'name': 'Jane', 'age': 22, 'tall': 168})
del student['age']
print(student)

tall = student.pop('tall')

print(student)
print(tall)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)
