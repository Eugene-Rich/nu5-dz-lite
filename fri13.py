import datetime

def proc_fri13():

    kptn = int(input('Сколько ближайших пятниц 13-го вы хотите увидеть ? '))

    # Начинаем с текущей даты

    dt_now = datetime.datetime.now()

    dne = 1
    while True:
        future_date = dt_now + datetime.timedelta(days=dne)
        dn_mes = future_date.day
        dn_ned = future_date.weekday()
        if dn_mes == 13 and dn_ned == 4:
            print(future_date.year, future_date.month, future_date.day, sep='-')
            kptn = kptn - 1
            if kptn <= 0:
                break
        dne = dne + 1