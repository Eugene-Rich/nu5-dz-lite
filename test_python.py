import math

# В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot.
# Чем больше тестов на каждую функцию - тем лучше

def test_filter_01():

    numb1 = [1, 2, 4, 5, 7, 8, 10, 11]
    numb2 = [2, 4, 8, 10]
    assert list(filter(lambda x : x % 2 == 0,  numb1)) == numb2

def test_filter_02():

    numb1 = [1, 2, 4, 5, 7, 8, 10, 110]
    numb2 = [110]
    assert list(filter(lambda x : x > 100,  numb1)) == numb2

def test_map_01():

    numb1 = [1, 2, 4, 5, 7, 8, 10, 11]
    numb2 = [2, 4, 8, 10, 14, 16, 20, 22]
    assert list(map(lambda x : x * 2,  numb1)) == numb2

def test_map_02():

    numb1 = ['a', 'b', 'c']
    numb2 = ['aa', 'bb', 'cc']
    assert list(map(lambda x : x * 2,  numb1)) == numb2

def test_sort_01():

    numb1 = [11, 2, 4, 5, 7, 8, 10, 1]
    numb2 = [1, 2, 4, 5, 7, 8, 10, 11]
    numb1.sort()
    assert numb1 == numb2

def test_sort_02():

    numb1 = [1, 2, 4, 5, 7, 8, 10, 11]
    numb2 = [2, 4, 8, 10, 1, 5, 7, 11]
    numb1.sort(key=lambda x : x % 2)
    assert numb1 == numb2

def test_pi_01():

    spi = str(math.pi)
    assert spi[0:4] == '3.14'

def test_pi_02():

    vpi = math.pi
    assert type(vpi) is float

def test_sqrt_01():

    assert math.sqrt(25) == 5

def test_sqrt_02():

    rez = math.sqrt(25)
    assert type(rez) is float

def test_pow_01():

    for i in range(1, 10):
        rez1 = math.pow(i, i)
        rez2 = i ** i
        assert rez1 == rez2

def test_hypot_01():

    for i in range(1, 10):
        x = i
        y = i + 1
        rez1 = math.hypot(x, y)
        rez2 = math.sqrt(x * x + y * y)
        assert round(rez1, 5) == round(rez2, 5)


test_filter_01()
test_filter_02()
test_map_01()
test_map_02()
test_sort_01()
test_sort_02()
test_pi_01()
test_pi_02()
test_sqrt_01()
test_sqrt_02()
test_pow_01()
test_hypot_01()