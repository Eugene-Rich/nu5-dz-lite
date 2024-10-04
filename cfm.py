import os
import shutil

import my_sch
from fri13 import proc_fri13
from victory import proc_v

def decorator_function(func):
    def inner():
        print('-')
        vl = func()
        print('\n'.join(vl))
        print('-' * 20)
    return inner

def create_dir(nrc):
    os.mkdir(nrc)
def delete_dir_f(nrc):
   shutil.rmtree(nrc)
def copy_dir_f(cish, cdist):
    shutil.copytree(cish, cdist)
@decorator_function
def view_dir_f():
    listfa = [file.name for file in os.scandir()]
    os.scandir().close()
    return listfa
@decorator_function
def view_f():
    listfa = [file.name for file in os.scandir() if os.path.isfile(file)]
    os.scandir().close()
    return listfa
@decorator_function
def view_d():
    listfa = [file.name for file in os.scandir() if os.path.isdir(file)]
    os.scandir().close()
    return listfa

def view_inf_os():
    return(os.name)

def view_avt():
    return ('Евгений Попов')

def chan_dir(nrc):
    try:
        os.chdir(nrc)
        return True
    except FileNotFoundError:
        return False



print ('Консольный файловый менеджер')
print('--------------------------------------------------------------------------------------------')
print('1. Создать папку                                  2. Удалить (файл/папку')
print('3. Копировать (файл/папку                         4. Просмотр содержимого рабочей директории')
print('5. Посмотреть только папки                        6. Посмотреть только файлы')
print('7. Просмотр информации об операционной системе    8. Создатель программы')
print('9. Играть в викторину                             10.Мой банковский счет')
print('11.Смена рабочей директории                       12.Ближайшие даты пятниц 13 числа')
print('13.Выход')

while True:
    vnc = input('Введите номер команды : ')
    if vnc == '1':
        nrc = input('Введите имя каталога : ')
        create_dir(nrc)
        print('Каталог создан.')
    elif vnc == '2':
        nrc = input('Введите имя каталога : ')
        delete_dir_f(nrc)
        print('Каталог удален.')
    elif vnc == '3':
        cish = input('Введите имя исходного каталога : ')
        cdist = input('Введите имя конечного каталога : ')
        copy_dir_f(cish, cdist)
        print('Каталог скопирован.')
    elif vnc == '4':
        view_dir_f()
    elif vnc == '5':
        view_d()
    elif vnc == '6':
        view_f()
    elif vnc == '7':
        print(view_inf_os())
    elif vnc == '8':
        print(view_avt())
    elif vnc == '9':
        proc_v()
    elif vnc == '10':
        my_sch.osn_prg_sch()
    elif vnc == '11':
        nrc = input('Введите имя каталога : ')
        print('Текущий каталог изменен.' if chan_dir(nrc) else 'Нет такого каталога.')
    elif vnc == '12':
        proc_fri13()
    elif vnc == '13':
        break
