# MATHEUS LUIZ TEIXEIRA SILVA 11311EMT025

import os

print(dir(os))
print(os.getcwd())
os.chdir('E:/UFU/2021/2021.1')
print(os.getcwd())

os.chdir('E:/UFU/2021/2021.1/SD - Sistemas Digitais/GitHub/Semana02')
print(os.getcwd())

os.mkdir('teste')
os.makedirs('teste1/teste2')
os.rmdir('teste')
os.removedirs('teste1/teste2')

print(os.listdir())

os.rename('teste.txt', 'teste0.txt')
print(os.listdir())

import os
print(os.stat('teste0.txt').st_size)

import os
from datetime import datetime
os.chdir('E:/UFU/2021/2021.1/SD - Sistemas Digitais/GitHub/Semana02/')

for dirpath, dirnames, filenames in os.walk('E:/UFU/2021/2021.1/SD - Sistemas Digitais/GitHub/Semana02/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)


import os
from datetime import datetime
print(os.path.exists('tbm/testealgumacoisa.txt'))