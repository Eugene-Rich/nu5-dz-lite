
def popopln(ost):
    sumpop = int(input('Введите сумму пополнения счета : '))
    ost = ost + sumpop

def pokupka(ost, histst):
    sumpok = int(input('Введите сумму покупки : '))
    if sumpok > ost:
        opis_pok = input('Введите название покупки : ')
        newrec = [opis_pok, sumpok]
        histst.append(newrec)
        ost = ost - sumpok
    else:
        print('Денег не хвататет !')

def vivist(histst):
    print('История покупок.')
    for elhst in histst:
        print(elhst[0], elhst[1])

def osn_prg_sch():

    histst = []
    ost = 0

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню : ')
        if choice == '1':
            popopln(ost)
        elif choice == '2':
            pokupka(ost, histst)
        elif choice == '3':
            vivist(histst)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
