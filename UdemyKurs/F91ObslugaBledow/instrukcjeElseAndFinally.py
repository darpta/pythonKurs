import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input('How many persons are there in the team? ')
    persons = int(personsStr)
    tasksPerPerson = tasks / persons

except ValueError as e:
    print('Sorry - you need to enter the integer number:',e)
except ZeroDivisionError as e:
    print('Sorry - you need to enter value > 0:',e)    
except:
    print('Something went wrong...',sys.exc_info()[0])

# else wykona sie gdy nie dojdzie do zadnego bledu
else:                                           
    print('Every person should have around', tasksPerPerson, 'tasks')

# finally wykona sie zawsze
finally:
    print('Script finished with/without errors')


# zadania
'''
ZADANIE 1
Zaimportuj moduł os
Przeczytaj od użytkownika informację, którą można zinterpretować jako liczbę, np. zapytaj o akceptowalną cenę zakupu kolejnego kursu na Udemy. Wynik zapamiętaj w zmiennej line
Przeczytaj od użytkownika ścieżkę do pliku
Bez żadnej dodatkowej kontroli zapisz linię w pliku o wskazanej ścieżce
Przetestuj działanie skryptu podając ścieżkę do pliku który można utworzyć (np. ścieżka do nieistniejącego pliku w istniejącym katalogu) oraz podając ścieżkę, której nie można utworzyć (np ścieżka do nieistniejącego pliku w nieistniejącym katalogu). Zauważ jaki błąd jest wyświetlany w drugim przypadku

ZADANIE 2
Zmodyfikuj poprzedni przykład tak, że instrukcje wykonujące operacje na pliku znajdą się w bloku try
Jeżeli dojdzie do błedu wyświetl komunikat "SORRY - WE HAVE AN ERROR"
Wykonaj testy takie jak poprzednio

ZADANIE 3
Dodaj instrukcję except, która wychwyci błąd FileNotFoundError:
W przypadku tego specyficznego błędu wyświetl komunikat "Error opening file". Możesz dodać szczegółowe informacje o błędzie

ZADANIE 4
Jako ostatnią instrukcję w bloku try dodaj konwersję wartości zapamiętanej w zmiennej line na typ int. Zapamiętaj wynik w zmiennej value
Wyświetl informację "The value saved in file is...."
Przetestuj program na kilka sposobów: wartość która się konwertuje na liczbę lub nie, ścieżka, która istnieje lub nie itp.

ZADANIE 5
Dodaj kolejną instrukcję except obsługującą błąd ValueError, który może być wygenerowany podczas konwersji line na value.
W przypadku tego błędu wyświetl komunikat "The value entered cannot be converted to a number". Możesz wyświetlić więcej szczegółów o błędzie
Dodaj blok else, w którym będzie wyświetlony komunikat "Actions completed successfully"
Przetestuj działanie skryptu generując różne błędy
'''
  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
file = open(filepath,'w+')
file.write(line)
file.close()

#####################
  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')

#####################
  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')

#####################
  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    value = int(line)
    file.close()
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')

#####################
  
line = input('Enter accepted price: ')
filepath =input('Enter filename : ')
 
try:
    file = open(filepath,'w+')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is',value)
except FileNotFoundError as e:
    print('Error opening file',filepath,e)
except ValueError as e:
    print('The value entered cannot be converted to a number',line,e)
except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN')
else:
    print('Actions completed successfully')