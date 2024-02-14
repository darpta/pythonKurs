# Od wersji 3.7 pojawiają  się pewne zmiany w pracy z funkcja clock() z modułu time. Otóż ta funkcja nie jest już dostępna. Zamiast clock() należy korzystać z innych funkcji.

# import time
 
# sprawdzenie wersji pythona
# import sys
# print(sys.version)
 
# zamiast
# print(time.clock(), time.localtime(time.clock()))
# korzystaj z funkcji time.perf.counter():
# print(time.perf_counter(), time.localtime(time.perf_counter()))


### playing with time

import time

print('Current time is... unix epoch\n', time.time()) # czas liczony od 1.1.1970
print('Current time is... tuple\n', time.localtime(time.time()))
print('Current time is... for human\n', time.asctime(time.localtime(time.time())))
print('Current time is... for human\n', time.localtime(time.perf_counter())) # nie jest to biezacy czas
print('\n\n\n')


### playing with calendar

import calendar
print('-------------------------------------------------')
print(calendar.month(2017,9,w=5,l=2))
print('-------------------------------------------------')
print(calendar.month(2017,9))
print('-------------------------------------------------')
print('week day is',calendar.weekday(2017,9,29)) # dzien liczony jak index od 0
print('-------------------------------------------------')
calendar.setfirstweekday(6)
print('-------------------------------------------------')
print(calendar.month(2017,9,w=5,l=2))
print('-------------------------------------------------')
print(calendar.month(2017,9))
print('-------------------------------------------------')
print('week day is',calendar.weekday(2017,9,29))
print('-------------------------------------------------')
print('is 2020 a leap year?',calendar.isleap(2020)) # czy 2020 jest rokiem przestepnym
print('-------------------------------------------------')
print('Leap days 2000-2017',calendar.leapdays(2000,2017))
print('Leap days 2000-2020',calendar.leapdays(2000,2020)) # zakres funkcji obejmuje lata 2000-2019
print('Leap days 2000-2021',calendar.leapdays(2000,2021)) # tutaj zakres funkcji uwzglednia 2020

print(calendar.calendar(2024))


# zadania

'''
1. Zaimportuj modul time (zrobione wyzej)

2. Wyświetl czas (datę i godzinę) w postaci Unix Epoche (skorzystaj z metody time)

3. Wyświetl czas (datę i godzinę) w postaci czytelnej dla człowieka. W tym celu złóż metodę localtime z metodą time

4. Zaimportuj moduł calendar (zrobione wyzej)

5. Każdy z nas ma swoje ważne daty: datę urodzenia swoją, dziewczyny/chłopaka, dziecka, data przyjęcia do pierwszej pracy, data zakończenia podstawówki itp. Wyświetl miesiąc zawierający tą datę

6. Zmień sposób wyświetlenia daty tak, aby niedziela była pierwszym dniem tygodnia

7. Wyświetl miesiąc z ważną dla Ciebie datą ponownie

8. Sprawdź czy rok 2000 był przestępny

9. Wyświetl kalendarz za rok 2019 i zobacz czy układ świąt Bożego Narodzenia wygląda atrakcyjnie czy nie
'''

print(time.time())
print(time.localtime(time.time()))
 
 
print(calendar.month(2000,8))
calendar.setfirstweekday(6)
print(calendar.month(2000,8))
 
print('2000 is leap: ', calendar.isleap(2000))
 
print(calendar.calendar(2019))