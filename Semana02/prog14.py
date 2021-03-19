# MATHEUS LUIZ TEIXEIRA SILVA 11311EMT025

import os

os.chdir('E:/UFU/2021/2021.1/SD - Sistemas Digitais/GitHub/Semana02') #diretório dos programas
print(os.getcwd())

#separar os nomes e fazer modificações
for f in os.listdir():

    f_name, f_ext = os.path.splitext(f)
    print(f_name)
    
    f_title, f_num = f_name.split('-')
    
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    
    print('{}-{}{}'.format(f_num, f_title, f_ext))

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)

    os.rename(f, new_name)