# MATHEUS LUIZ TEIXEIRA SILVA 11311EMT025

courses = ['History', 'Mat', 'Physics', 'CompSci']

print(courses)
print(len(courses))

print(courses[1])
print(courses[3])
print(courses[-1])

#print(courses[4]) #out of range

print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('Art')
print(courses)

courses.insert(0,'Art')
print(courses)

courses = ['History', 'Mat', 'Physics', 'CompSci']
courses2 = ['Art', 'Education']

courses.insert(0, courses2) #errado
print(courses)

courses = ['History', 'Mat', 'Physics', 'CompSci']
courses2 = ['Art', 'Education']

courses.extend(courses2)
print(courses)

courses.remove('Mat')
print(courses)


courses = ['History', 'Mat', 'Physics', 'CompSci']
popped = courses.pop()
print(popped)
print(courses)

courses = ['History', 'Mat', 'Physics', 'CompSci']
courses.reverse()
print(courses)

courses = ['History', 'Mat', 'Physics', 'CompSci']
courses.sort()
print(courses)


nums = [1, 5, 2, 4, 3 ]
courses.sort()
nums.sort()
print(courses)
print(nums)

nums = [1, 5, 2, 4, 3 ]
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

courses = ['History', 'Mat', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3 ]
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

courses = ['History', 'Mat', 'Physics', 'CompSci']
print(courses.index('CompSci'))
#print(courses.index('Art'))
print('Art' in courses)
print('Mat' in courses)

for item in courses:
    print(item)

for course in courses:
    print(course)

for index, course in enumerate(courses, start=1):
    print(index, course)

courses = ['History', 'Mat', 'Physics', 'CompSci']
course_str = ', '.join(courses)
print(course_str)

courses = ['History', 'Mat', 'Physics', 'CompSci']
course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

list_1 = ['History', 'Mat', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


tuple_1 = ('History', 'Mat', 'Physics', 'CompSci')
tuple_2 = tuple_1

#tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

cs_courses = {'History', 'Mat', 'Physics', 'CompSci'}
print(cs_courses)

cs_courses = {'History', 'Mat', 'Physics', 'CompSci', 'Mat'}
print(cs_courses)

cs_courses = {'History', 'Mat', 'Physics', 'CompSci', 'Mat'}
print('Mat' in cs_courses)

cs_courses = {'History', 'Mat', 'Physics', 'CompSci'}
art_courses = {'History', 'Mat', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} #errado
empty_set = set()

#teste
print(empty_list)
print(empty_tuple)
print(empty_set)