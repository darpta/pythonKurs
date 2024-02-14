import datetime

print('Minimum and maximum',datetime.MINYEAR, datetime.MAXYEAR)

# from datetime import timedelta
d1 = datetime.timedelta(days=1,hours=2,minutes=-30)
print(d1)

d2 = datetime.timedelta(days=-1,hours=-2,minutes=-3)
print(d2)

print('timedelta sum:',d1+d2)

print('-------------------------------------------------\n')

# from datetime import date

print('Today is', datetime.date.today(),'\n')

today = datetime.date.today()
daysToPay = datetime.timedelta(days=7)
print('Today is', today)
print('Bills should be paid within:',daysToPay.days,'days')
print('The bill should be paid till:',today + daysToPay,'\n')

endOfTheWorld = datetime.date.max
print('The final end of the world will happen (by Python):',endOfTheWorld)
print(endOfTheWorld.weekday(),'\n')

bornDate = datetime.date(2000,8,15)
today = datetime.date.today()
print(today - bornDate,'\n')

print('-------------------------------------------------\n')

# from datetime import datetime

print('now()\t',datetime.datetime.now())
print('today()\t',datetime.datetime.today())
print('utcnow()\t',datetime.datetime.now(datetime.UTC)) # nowa wersja
print('weekday()\t',datetime.datetime.today().weekday(),'\n')

print('%a',datetime.datetime.now().strftime('%a'))
print('%A',datetime.datetime.now().strftime('%A'))
print('%w',datetime.datetime.now().strftime('%w'))
print('%a %A %w ',datetime.datetime.now().strftime('%a %A %w'))
print('%Y-%m-%d_%H_%M_%S_%f',datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S_%f'))