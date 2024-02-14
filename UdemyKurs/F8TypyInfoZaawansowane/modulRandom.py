import random

# komentarze w liniach kodu :-)
print('One random number:',random.randint(1,100),'\n') #   1 <= N <= 100
#print('\n')

print('Chosing random number from a range',random.choice(range(1,100)))
print('\n')

print('Chosing random number from a range - easier',random.randrange(1,100))
print('\n')

list = ['John','Ann','Peter','Susan','Emily','Greg','Chris']
random.shuffle(list)
print('Reordered list:',list)
print('\n')

print('Just a random float:',random.random())
print('\n')


# zadania

'''
1. Zaimportuj moduł random (zrobione wyzej)

2. Wylosuj 10 liczb z zakresu 1-100

3. To nieco dłuższe zadanie:
    do zmiennej number1 wylosuj liczbę całkowitą z zakresu 1-100
    twoim celem będzie losowanie liczb losowych tak długo, aż znowu wylosujesz liczbę number1. Dodatkowo chcemy policzyć ile prób jest do tego potrzebnych
    do zmiennej counter zapisz 1
    do zmiennej number2 wylosuj liczbę z zakresu 1-100
    wyświetl numer próby (counter) i wylosowaną liczbę (number2)
    Tak długo jak długo number1 jest inne niż number2
        zwiększ counter o 1
        wylosuj ponownie liczbę number2 (liczba całkowita od 1 do 100)
        wyświetl numer próby (counter) i wylosowaną liczbę (number2)
    Na zakończenie wyświetl podsumowanie z infromacją o ilości prób

4. Tym razem zbudujesz program losujący skład do rozgrywek "2018 FIFA WORLD CUP RUSSIA". Utwórz zmienną countries jak poniżej:
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
następnie:
losowo wymieszaj kolejność drużyn
utwórz zmienną groupNumber i przypisz jej wartość 0
wykonaj czynność tyle razy ile jest państw na liście countries:
    jeżeli numer państwa jest podzielny przez 4 (reszta z dzielenia modulo 4 jest równa 0) to:
        zwiększ numer grupy o 1
        wyświetl napis "----Grupa X----"
    każdorazowo wyświetlaj wylosowany kraj
Jak sądzisz, czy w Twojej konfiguracji grup Polska miałaby większe szanse?
'''

for i in range(10):
    print(random.randint(1,100))
    
########################
 
number1 = random.randint(1,100)
print("The first generated number is %d" %(number1))
 
counter = 1
number2 = random.randint(1,100)
 
while number1 != number2:
    counter+=1
    number2=random.randint(1,100)
    print(counter, number2)
    
print("I needed %d attempts to generate %d again" % (counter, number1))
 
########################
 
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
 
random.shuffle(countries)
 
groupNumber = 0
 
for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])