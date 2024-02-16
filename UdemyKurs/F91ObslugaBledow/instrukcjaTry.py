import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input('How many persons are there in the team? ')
    persons = int(personsStr)
    tasksPerPerson = tasks / persons
except:
    print('Something went wrong...',sys.exc_info()[0]) # sys.exc_info() podaje info o bledzie
    
print('Every person should have around', tasksPerPerson, 'tasks')


# zadanie
'''
Pamiętasz przykład, w którym przetwarzaliśmy dane o zamówieniach z aptek? Jeśli nie, to zajrzyj do laboratorium sprzed dwóch lekcji :)
Wczytywaliśmy tam dane z pliku, a potem przetwarzaliśmy linijka po linijce. Każda z linijek zawierała informacje o nazwie apteki, nazwie leku i ilości zamawianego leku.
Już w poprzednim rozwiązaniu spodziewaliśmy się pewnych problemów i zabezpieczaliśmy się przed nimi. Gdyby z apteki przyszło  zamówienie, które nie miało dokładnie 3 pól, to nie przetwarzaliśmy go, ale:
    właściwie obecność dodatkowej notatki w czwartej kolumnie wcale w niczym nie przeszkadza,
    może się zdarzyć, że w kolumnie ilość, zostanie przesłany tekst, którego nie można zinterpretować jako liczbę
    może się zdarzyć, że w linijce zabraknie jakiś kolumny
    i wreszcie.... co całkiem normalne - to my programiści możemy popełnić jakiś błąd.
Dlatego zajmiemy sie dokładniej instrukcją przetwarzającą zamówienie.
Umieść w pliku tekstowym orders.csv następujący tekst:
    Pharma A, Vitamin C,100
    Drugstore XYZ,Penicilin, 20, pills
    Drugstore ABC,Aspirin,60
    Pharma X,Montelukast,10
    Pharma at grocery,Amoxicillin,?
    Pharmacy 123,Cephalexin,100
    Pharmacy 123,Prednisolone Sodium Phosphate
    Pharma X,Nystatin,45
Zauważ błędy: linijka 2 - dodatkowa kolumna, linijka 5 - znak zapytania w kolumnie z ilością, linijka 7 - za mało kolumn

Zaczynamy od następującego skryptu - skopiuj go do swojego skryptu i następnie przerabiaj krok po kroku:

file_path = r'c:\temp\data_input\orders.csv'
with open(file_path,"r") as file:
    for line in file: 
        line = line.replace('\n','')
        order = line.split(',')
        # ADD YOUR CODE HERE
print("Processing finished")

Na początku skryptu zaimportuj moduł sys (jest potrzebny do ustalenia rodzaju błędu)
W miejscu oznaczonym komentarzem:
    w zmiennej pharmacy_name zapisz zerowy element listy order
    w zmiennej item zapisz pierwszy element listy order
    w zmiennej amount zapisz wynik konwersji do typu int dla drugiego elementu listy order
Wyświetl komunikat 'Order from drugstore "%s", item "%s", amount %d' zastępując pola na pharmacy_name, item i amount
Uruchom skrypt - co powinno zakończyć się katastrofą:
Order from drugstore "Pharma A", item " Vitamin C", amount 100
Order from drugstore "Drugstore XYZ", item "Penicilin", amount 20
Order from drugstore "Drugstore ABC", item "Aspirin", amount 60
Order from drugstore "Pharma X", item "Montelukast", amount 10
Traceback (most recent call last):
  File "C:/Users/rafal/AppData/Local/Programs/Python/Python35/orders_processing_error.py", line 25, in <module>
    amount = int(order[2])
ValueError: invalid literal for int() with base 10: '?'
5. Dodaj instrukcję try/except, która:
obsłuży błedy instrukcji opisanych w krokach 2-3
w przypadku błędu wyświetli linijkę, w której doszło do błędów oraz informacje na temat samego błędu
'''

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