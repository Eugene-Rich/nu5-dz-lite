import os
from cfm import savesrk

def test_saversk1():

    list_files = []
    for file in os.scandir():
        if os.path.isfile(file):
            list_files.append(file.name)
    os.scandir().close()

    assert set(savesrk(1)) == set(list_files)

def test_saversk2():
    list_dirs = []
    for file in os.scandir():
        if os.path.isdir(file):
            list_dirs.append(file.name)
    os.scandir().close()

    assert set(savesrk(2)) == set(list_dirs)

test_saversk1()
test_saversk2()