# MATHEUS LUIZ TEIXEIRA SILVA 11311EMT025

student ={'name': 'John', 'age': 25, 'courses':['Mat', 'Compsci']}
print(student)
print(student['name'])
print(student['courses'])

student ={1: 'John', 'age': 25, 'courses':['Mat', 'Compsci']}
print(student[1])

student ={'name': 'John', 'age': 25, 'courses':['Mat', 'Compsci']}
print(student)
#print(student['phone'])  #errado

student ={'name': 'John', 'age': 25, 'courses':['Mat', 'Compsci']}
print(student)
print(student.get('phone','Not Found'))

student ={'name': 'John', 'age': 25, 'courses':['Mat', 'Compsci']}
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student)

student.update({'name': 'Jane', 'age': 26, 'phone':'555-5555'})
print(student)

student ={'name': 'John', 'age': 25, 'courses':['Mat', 'Compsci']}
del student['age']
print(student)

student ={'name': 'John', 'age': 25, 'courses':['Mat', 'Compsci']}
age = student.pop('age')
print(student)
print(age)
print(len(student))
print(student.keys())
print(student.items())

student ={'name': 'John', 'age': 25, 'courses':['Mat', 'Compsci']}

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
