
def popopln():
    sumpop = int(input('Введите сумму пополнения счета : '))
    return sumpop

def pokupka(ost, histst):
    sumpok = int(input('Введите сумму покупки : '))
    if sumpok <= ost:
        opis_pok = input('Введите название покупки : ')
        newrec = [opis_pok, sumpok]
        histst.append(newrec)
        return sumpok
    else:
        print('Денег не хвататет !')
        return 0

def vivist(histst):
    print('История покупок.')
    for elhst in histst:
        print(elhst[0], elhst[1])

def osn_prg_sch():

    try:
        with open('mscht.txt', 'r') as fsch:
            sst_ost = fsch.read()
            ost = int(sst_ost)
            fsch.close()
    except FileNotFoundError:
        ost = 0


    try:
        with open('fistp.txt', 'r', encoding='utf-8') as fistp:
            lines = fistp.readlines()
            histst = []
            for st in lines:
                vlst = st.split(',')
                histst.append([vlst[0], int(vlst[1])])
    except FileNotFoundError:
        histst = []


    while True:
        print('У вас на счете : ', ost)
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню : ')
        if choice == '1':
            ost = ost + popopln()
        elif choice == '2':
            sumpok = pokupka(ost, histst)
            ost = ost - sumpok
        elif choice == '3':
            vivist(histst)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

    fsch = open('mscht.txt', 'w')
    fsch.write(str(ost))
    fsch.close()

    fistp = open('fistp.txt', 'w', encoding='utf-8')
    for eist in histst:
        fistp.writelines(eist[0] + ',' + str(eist[1]) + '\n')
    fistp.close()

if __name__ == '__main__':
    ost = 0
    histst = []
    osn_prg_sch()

