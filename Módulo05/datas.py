
from datetime import datetime, timedelta

data = datetime(2022, 7, 6, 16, 21, 0)
data1 = datetime.strptime("20/05/1440", "%d/%m/%Y")
print(data.strftime('%d/%m/%Y  %H:%M:%S'))
print(data1)
print(data.timestamp())
data2 = datetime.fromtimestamp(1657135260.0)
print(data2)


d1 = datetime.strptime("20/05/2020 20:00:00", "%d/%m/%Y %H:%M:%S")
datadif = d1+timedelta(days=5)


from locale import setlocale, LC_ALL
import calendar


# Sexta, 14 de Julho de 2022

setlocale(LC_ALL, 'pt_BR.UTF-8')

dt = datetime.now()
formatacao = dt.strftime("%A, %d de %B de %Y")
print(formatacao)


mes_atual = datetime.today()
days_month = []
for x in range(1,13):
    daysInMonth= calendar.monthrange(2022, x)[1]
    days_month.append(daysInMonth)

print(days_month)
print(mes_atual)




