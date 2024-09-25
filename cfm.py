import os
import shutil

import my_sch
from fri13 import proc_fri13
from victory import proc_v

def create_dir():
    nrc = input('Введите имя каталога : ')
    os.mkdir(nrc)
def delete_dir_f():
    nrc = input('Введите имя каталога : ')
    shutil.rmtree(nrc)
def copy_dir_f():
    cish = input('Введите имя исходного каталога : ')
    cdist = input('Введите имя конечного каталога : ')
    shutil.copytree(cish, cdist)
def view_dir_f():
    for file in os.scandir():
        print(file.name)
    os.scandir().close()

def view_f():
    for file in os.scandir():
        if os.path.isfile(file):
            print(file.name)
    os.scandir().close()

def view_d():
    for file in os.scandir():
        if os.path.isdir(file):
            print(file.name)
    os.scandir().close()

def view_inf_os():
    print(os.name)

def view_avt():
    print('Евгений Попов')

def chan_dir():
    nrc = input('Введите имя каталога : ')
    try:
        os.chdir(nrc)
    except FileNotFoundError:
        print('Нет такого каталога.')


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
        create_dir()
    elif vnc == '2':
        delete_dir_f()
    elif vnc == '3':
        copy_dir_f()
    elif vnc == '4':
        view_dir_f()
    elif vnc == '5':
        view_d()
    elif vnc == '6':
        view_f()
    elif vnc == '7':
        view_inf_os()
    elif vnc == '8':
        view_avt()
    elif vnc == '9':
        proc_v()
    elif vnc == '10':
        my_sch.osn_prg_sch()
    elif vnc == '11':
        chan_dir()


    elif vnc == '12':
        proc_fri13()
    elif vnc == '13':
        break
