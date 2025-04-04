from datetime import datetime, date
# import datetime

mi_hora = datetime.time()
print(type(mi_hora))
print(mi_hora)

mi_dia = datetime.date(2025, 5, 2)
print(mi_dia.today().ctime())

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
print(mi_fecha)

mi_fecha = mi_fecha.replace(month=11)

print(mi_fecha)

nacimiento = date(1999, 10, 4)
defuncion = date(2025, 4, 2)
vida = (defuncion - nacimiento) / 365
print(vida)

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta
print(vigilia.seconds)

minutos = datetime.time()
print(minutos)

minutos = datetime.now().minute
print(minutos)