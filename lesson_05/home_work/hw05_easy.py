import os
import shutil
import sys
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_f(name, rep = None):
    if rep == None:
        m_k(name)
    else:
        for i in range(rep):
            m_k(f'{name}_{i+1}')


def m_k(f_n):
    d = os.path.join(os.getcwd(), f_n)
    try:
        os.mkdir(d)
        print(f'{d} file created!')
    except FileExistsError:
        print(f'{d} file already exists')


def d_d(f_n):
    d = os.path.join(os.getcwd(), f_n)
    if os.path.exists(d):
        os.rmdir(d)
        print(f'{d} deleted!')
    else:
        print(f'{d} file not found')

def delete_f(name, rep = None):
    if rep == None:
        d_d(name)
    else:
         for i in range(rep):
            d_d(f'{name}_{i+1}')


# create_f('dir', 9)
# delete_f('dir', 9)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def view_d():
    return [i for i in os.listdir() if os.path.isdir(i)]
# print(view_d())


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_f():
    shutil.copy(sys.argv[0], f'{os.getcwd()}\\copy.py')

# copy_f()

