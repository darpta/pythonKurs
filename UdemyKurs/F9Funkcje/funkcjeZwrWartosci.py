from datetime import date
from datetime import timedelta

def GiveWorkingDay(year = date.today().year,
                    month = date.today().month,
                    day = date.today().day):
  
    day = date(year, month, day)

    if day.weekday() == 5: # sobota bo index 6
        workingday = day + timedelta(days=2) # aby uzyskac dzien roboczy trzeba dodac 2 dni
    elif day.weekday() == 6: # niedziela bo index 7
        workingday = day + timedelta(days=2) # aby uzyskac dzien roboczy trzeba dodac 1 dzien
    else:
        workingday = day        

    return workingday

nextworkingday = GiveWorkingDay(2017,9,3)
print('Next working day after',2017,9,3,'is',nextworkingday)
nextworkingday = GiveWorkingDay()
print('Next working day after today is',nextworkingday)

print('Next working day after today is',GiveWorkingDay())

# zadania
'''
ZADANIE 1
Nadal pracujemy nad tymi samymi funkcjami, co poprzednio. Zaczynamy od funkcji PrintAnimal. Należy zwrócić informację o tym czy obrazek został wyświetlony, czy nie:
    Jeżeli przekazano poprawny parametr i obrazek został wyświetlony, należy zrócić wartość True
    Jeżeli przekazano niepoprawny parametr i obrazek nie został wyświetlony, należy zwrócić False
Przetestuj działanie funkcji po zmianie

ZADANIE 2
Teraz modyfikujemy funkcję DaysToEndOfYear. Ilość dni do Sylwestra nie ma być wyświetlana, ale zamiast tego zwracana. Przetestuj działanie funkcji
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
        return False
    
    return True
 
 
if PrintAnimal():
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
 
if PrintAnimal('dog'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
 
if PrintAnimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')

########################

from datetime import date
 
def DaysToEndOfYear(year = date.today().year,
                    month = date.today().month,
                    day = date.today().day):
    
    date_today = date(year,month,day)
    date_end_year = date(year, 12, 31)
    delta = date_end_year - date_today
    return delta.days
 
print('Date: 2020-12-20 days to end of year: %d' %(DaysToEndOfYear(2020,12,20)))
 
print('Date: 2020-12-21 days to end of year: %d' %(DaysToEndOfYear(2020,12,21)))
 
print('Date: TODAY days to end of year: %d' %(DaysToEndOfYear()))