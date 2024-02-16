def GiveWorkingDay(year, month, day):
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

GiveWorkingDay(2017,10,1)
GiveWorkingDay(2017,9,30)
GiveWorkingDay(day=30,year=2017,month=9)

# zadania
'''
ZADANIE 1
W tym zadaniu zmodyfikujemy funkcję z wcześniejszego laboratorium. Poniżej znajdziesz moje propozycje trzech funkcji.Każda z nich robiła inną rzecz, ale wszystkie są do siebie podobne. Zastąpimy je jedną funkcją, która przyjmie parametr i w zależności od tego parametru wyświetli inny "obrazek":
    zadeklaruj funkcję PrintAnimal
    zdefiniuj przekazywany parametr o nazwie animal
        jeżeli animal to 'cat', to wyświetl obrazek kota
        jeżeli animal to 'bear', to wyświetl obrazek misia
        jeżeli animal to 'bat', to wyświetl obrazek nietoperza
        a jeżeli wartość jest zupełnie inna, to wyświetl komunikat: "Cannot print '%s'. Correct values for the parameter are: cat, bear, bat", zastępując %s napisem przekazanym w animal
    Przetestuj wywołanie funkcji przekazując różne wartości argumentu, czasami przez pozycję, a czasami przez nazwę. Przekazuj poprawne i niepoprawne parametry (ale póki co tylko napisy - nie np. liczby)
    Oto funkcje do przeróbki:

def PrintCat()
def PrintBear()
def PrintBat()

ZADANIE 2
Oto kolejna przeróbka już istniejącej funkcji. W poprzednim laboratorium pisaliśmy funkcję obliczającą ile dni zostało do Sylwestra od dnia dzisiejszego. Zmień funkcję tak, aby:
    przyjmowała parametry: year, month, day
    w pierwszej kolejności konwertuje przekazane liczby na datę
    oblicza ile dni musi minąć od tej daty do najbliższego Sylwestra
    (na tym etapie nie sprawdzamy poprawności daty)
    przetestuj działanie funkcji z różnymi parametrami przekazując argumenty przez wartość lub przez nazwę. Podczas przekazywania parametrów przez nazwę zmieniaj kolejność parametrów np rok/miesiąc/dzień lub dzień/miesiąc/rok

Oto funkcja do przeróbki:

def DaysToEndOfYear():
    from datetime import date
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
'''

def PrintAnimal(animal):
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
 
PrintAnimal('cat')
PrintAnimal(animal='bear')
PrintAnimal(animal='bat')
PrintAnimal('unicorn')

#################################

def DaysToEndOfYear(year, month, day):
    from datetime import date
 
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
 
DaysToEndOfYear(2020,12,20)
DaysToEndOfYear(2021,12,21)
DaysToEndOfYear(year = 2022, month = 12, day = 22)
DaysToEndOfYear(day = 23, month =12, year = 2023)