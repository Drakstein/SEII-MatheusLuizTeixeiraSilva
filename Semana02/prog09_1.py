import prog09_0

courses = ['History', 'Math', 'Physics', 'CompSci']

index = prog09_0.find_index(courses, 'Physics')
print(index)


import prog09_0 as pg9

courses = ['History', 'Math', 'Physics', 'CompSci']

index = pg9.find_index(courses, 'Physics')
print(index)


from prog09_0 import find_index, test
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Physics')
print(index)
print(test)

from prog09_0 import find_index, test

import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Physics')

print(sys.path)


#não é o melhor jeito
import sys
sys.path.append('/E:/UFU/2021/2021.1/SD - Sistemas Digitais/GitHub')

from prog09_0 import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Physics')

print(sys.path)

import math

rads = math.radians(45)

print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

import os

print(os.getcwd())

#lembrar de anotar os módulos mais comuns

print(os.__file__)


import antigravity #vai abrir uma página xD
