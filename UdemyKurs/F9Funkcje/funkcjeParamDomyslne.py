def GiveWorkingDay(year=2017, month=1, day=1): # day jako parametr domyslny ustawiony na 1
    # prints the nearest working day date    
    from datetime import date
    from datetime import timedelta

    day = date(year, month, day)

    if day.weekday() == 5: # sobota bo index 6
        workingday = day + timedelta(days=2) # aby uzyskac dzien roboczy trzeba dodac 2 dni
    elif day.weekday() == 6: # niedziela bo index 7
        workingday = day + timedelta(days=2) # aby uzyskac dzien roboczy trzeba dodac 1 dzien
    else:
        workingday = day        
    print('working day for',day,'is',workingday)
    return

GiveWorkingDay(2017,10) # nie podano wartosci dla day, wiec day=1
GiveWorkingDay(2017,10,2) # wartosc dla day ustawiona, wiec day=2
# tak samo dla month i year
GiveWorkingDay()


# zadania
'''
ZADANIE 1
Nadal kontynuujemy pracę nad poprzednio tworzonymi funkcjami. Funkcja PrintAnimal(animal) wyświetla obrazek odpowiadający przekazanemu parametrowi. A co jeśli żaden parametr nie zostanie przekazany? Obecnie funkcja wyświetli błąd.
Zmień to. Jeżeli żaden parametr nie został przekazany, to parametr animal ma być zainicjowany napisem pustym. Po zmianie wywołaj funkcję przekazując parametr lub go opuszczając. W przypadku opuszczenia parametru powinien zostać wyświetlony komunikat wskazujący na poprawne wartości parametru.

ZADANIE 2
Funkcja DaysToEndOfYear(year, month, day) z poprzedniego laboratorium też wymaga drobnej poprawki
Jeżeli któryś z parametrów został opuszczony podczas wywołania, to należy podstawić rok, miesiąc lub dzień z daty dzisiejszej. Przetestuj wywołanie funkcji na różne sposoby
Uwaga! Ponieważ operacje na dacie trzeba wykonać jeszcze przed samą definicją funkcji (mówimy o tym "w sygnaturze funkcji"), to polecenie importujące moduł datetime trzeba przesunąć z definicji funkcji (ciała funkcji) na początek skryptu. Pozwoli to na korzystanie z funkcji date.today()
'''

def PrintAnimal(animal = ''):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
 
    if animal == 'cat':
        print(txt_cat)
    elif animal == 'bear':
        print(txt_bear)
    elif animal == 'bat':
        print(txt_bat)
    else:
        print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
    
    return

###########################

from datetime import date
 
def DaysToEndOfYear(year = date.today().year,
                    month = date.today().month,
                    day = date.today().day):
    
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print('Counting from ', date_today,'days remaining', delta.days)
 
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(day = 23, month =12, year = 2023)
DaysToEndOfYear()
DaysToEndOfYear(year=2020)
DaysToEndOfYear(year=2020, month=10)
DaysToEndOfYear(day=1)
