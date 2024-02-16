import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input('How many persons are there in the team? ')
    persons = int(personsStr)
    tasksPerPerson = tasks / persons

# roznicowanie zachowanie skryptu w zaleznosci od tego do jakiego bledu doszlo
except ValueError as e:
    print('Sorry - you need to enter the integer number:',e)
except ZeroDivisionError as e:
    print('Sorry - you need to enter value > 0:',e)    
except:
    print('Something went wrong...',sys.exc_info()[0]) # sys.exc_info() podaje info o bledzie


print('Every person should have around', tasksPerPerson, 'tasks')


# zadanie
'''
Wracamy do przykładu z zamówieniami dla aptek. Obecnie sktypt potrafi już obsłużyć błędne pozycje zamówień, ale robi to w dość ogólny sposób - po prostu mówi, że ma problem z konwersją danej linijki, nie wnikając w to, co się tam złego zadziało. Spróbujemy to zmienić. Pracujemy nadal z tym samym plikiem, co poprzednio.
Oto skrypt w aktualnej postaci:

import sys
 
file_path = r'c:\temp\data_input\orders.csv'
 
with open(file_path,"r") as file:
    for line in file:
        line = line.replace('\n','')
        order = line.split(',')
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])
print("Processing finished")

1. Uruchom skrypt tak jak jest. Zauważ dwie kategorie błędów:
ValueError - związany z tym, że konwersja danych w trzeciej kolumnie się nie udaje
IndexError - związany z tym, że linijka ma za mało danych, po podziale linijki ze względu na przecinek otrzymujemy np. tylko listę dwuelementową, a potem próbujemy się odwołać do elementu spoza zakresu: orders[2]

2. Dodamy instrukcje rozpoznające te dwa przypadki i spróbujemy zasugerować, co administrator powinien sprawdzić (i poprawić) w pliku wejściowym:
przed linijką except, dodaj nową instrukcję except, która obsłuży błąd ValueError oraz spowoduje zapamiętanie informacji o błędzie w zmiennej e. Następnie wyświetl komunikat mówiący o tym, że doszło do błędu związanego z niepoprawną konwersją danych w trzecim polu do typu int. W komunikacie o błędzie wyświetl treść linijki z pliku tekstowego, która spowodowała błąd
dodaj kolejną instrukcję except, która obsłuży błąd IndexError oraz spowoduje zapamiętanie informacji o błędzie w zmiennej e. Następnie wyświetl komunika mówiący o tym, że doszło do błędu związanego z brakiem dostatecznej ilośći pól. W komunikacie wyświetl treść linijki z pliku tekstowego, która spowodowała błąd
'''
# skrypt z tresci zadania
import sys
 
file_path = r'c:\temp\data_input\orders.csv'
 
with open(file_path,"r") as file:
    for line in file:
        line = line.replace('\n','')
        order = line.split(',')
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])
print("Processing finished")

######## rozwiazanie #########

import sys
 
file_path = r'c:\temp\data_input\orders.csv'
 
 
with open(file_path,"r") as file:
 
    for line in file:
        line = line.replace('\n','')
        order = line.split(',')

        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))
        except ValueError as e:
            print("Problem with conversion. Check whether the amount is correct. Line: %s" % line)
        except IndexError as e:
            print("Missing information. Check whether the line is build of at least 3 fields separated by comma. Line: %s" % line)
        except:
            print("General error: %s" % sys.exc_info()[0])
            
print("Processing finished")