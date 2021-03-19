# MATHEUS LUIZ TEIXEIRA SILVA 11311EMT025

if True:
    print('Conditional was True')

if False:
    print('Conditional was True')

language = 'Python'
if language =='Python':
    print('Conditional was True, Yes python!')

language = 'Python'
if language =='Python':
    print('Language is Python')
else:
    print('No match')

language = 'Java'
if language =='Python':
    print('Language is Python')
elif language =='Java':
    print('Language is Java')
elif language =='Javascript':
    print('Language is Java')
else:
    print('No match')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')



user = 'Other'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')



user = 'Other'
logged_in = True

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

a = [1,2,3]
b = [1,2,3]

print(a == b)
print(id(a))
print(id(b))
print(a is b)

a = [1,2,3]
b = a

print(a == b)
print(id(a))
print(id(b))
print(id(a) == id(b))


condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = 11123

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = []

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ''

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


condition = 'alguma coisa'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')