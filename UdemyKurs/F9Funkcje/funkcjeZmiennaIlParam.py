def DoAction(action, parameter):
    print('action:',action)
    print('parameter:',parameter)
    return

DoAction('buy','shoes')


def DoAction2(action, *parameter): # * oznacza kolekcje wartosci
    print('action:',action)
    print('parameter:',parameter)
    for element in parameter:       # iteracja przez elementy
        print('element is',element)
    return

DoAction2('buy','shoes','socks') # parameter moze wyswietlic kolekcje wartosci
DoAction2('buy','shoes','socks','t-shirt')


def DoAction3(action, what, **parameter): # * oznacza kolekcje wartosci
    print('action:',action)
    print('what:',what)
    print('parameter:',parameter) # tu powstaje slownik, wiec iteracja przez elementy jest inna
    for element in parameter:       # iteracja przez elementy w slowniku
        print(element,'=',parameter[element])
    return

DoAction3('buy','shoes',size=45,color='brown',type='sport') # parameter stal sie slownikiem


# zadania
'''
ZADANIE 1
Nadal poprawiamy znane Ci funkcje. Zaczynamy od PrintAnimal.
Zmień definicję funkcji tak, aby można było przekazać zmienną ilość nazw zwierząt, które mają być narysowane. Na tym etapie rezygnujemy ze zwracania wartości oraz wartości domyślnej. Po zmianach przetestuj działanie funkcji przekazując po kilka nazw zwierząt jako parametr (wybieraj spośród tych zdefiniowanych w funkcji, jak i niepoprawnych)

ZADANIE 2
A teraz kolej na DaysToEndOfYear:
    zmień parametr tak, aby przyjmował wiele dat (uwaga funkcja będzie przyjmować daty, a nie osobne wartości rok/miesiąc/dzień)
    dla każdej daty z parametrów ma zostać wyświetlona informacja o dacie i ilości dni do Sylwestra
    usuń część funkcji odpowiadającą za zwracanie wartości
    przetestuj działanie funkcji przekazując różną ilość argumentów
'''

def PrintAnimal(*animals):
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
 
    for animal in animals:
        if animal == 'cat':
            print(txt_cat)
        elif animal == 'bear':
            print(txt_bear)
        elif animal == 'bat':
            print(txt_bat)
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
    
    return 
 
PrintAnimal('cat','bat')
print('-------------------------------------')
PrintAnimal('cat','bat','dog','bear')
print('-------------------------------------')
PrintAnimal()

######################################

from datetime import date
 
def DaysToEndOfYear(*dates):
 
    for date_today in dates:
        
        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print('Date', date_today, 'days to end of year', delta.days)
 
DaysToEndOfYear(date(1999,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15))
print('----------------')
DaysToEndOfYear(date(1999,1,15),date(2009,1,15),date(2019,1,15),date.today())