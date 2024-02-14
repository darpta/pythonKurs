i = 1
imax = 10

while i <= imax:    # warunek
    print(i,'I like Python')    # instrukcja
    i += 1  # inkrementacja, nie musi byc 1, --- dekrementacja i-=1
else:
    print('Now i =',i)


# zadania
    
'''
1. Tym razem pracujesz w LOT i masz za zadanie rozpocząć programowanie rozkładu miejsc w samolocie. (Patrz https://www.lot.com/pl/pl/boeing-737-800-rozklad-miejsc lub ilustracja na końcu tego laboratorium)
Należy wyświetlić napisy:
Row number 1
Row number 2
...
Row number 30
Row number 31
W tym celu:
zadeklaruj zmienną firstRow i przypisz jej wartość 1
zadeklaruj zmienną lastRow i przypisz jej wartość  31
zadeklaruj zmienną currentRow i przypisz jej wartość  firstRow
Dopóki currentRow jest mniejsze równe lastRow:
wyświetlaj napis "Row number...."
po wyświetleniu napisu zwiększaj currentRow o 1

2. Śni Ci się koszmar. Twój nauczyciel matematyki kazał Ci wypisać liczby od 1 do 13 i dla każdej liczby wyliczyć jej kwadrat i sześcian. Ponieważ nauczyciel nie zabronił używać Pythona, napisz pętlę, która dla liczb od 1 do 13 wyświetli kwadrat i sześcian tej liczby

3. Śni Ci się koszmar. Dziecko kuzynki zafascynowane informatyką  prosi Cię o wymienienie kolejnych potęg dwójki. Postanawiasz znowu skorzystać z Pythona. Napisz pętlę while, która dla kolejnych liczb całkowitych x  od 0 do 16 wyznaczy wartość dwa do potęgi x.

4. Czy wiesz, że polecenie:
5*'x'
wyświetli
xxxxx
Tym razem Twoja Babcia poprosiła Cię o wydrukowanie wzoru haftu krzyżykowego w następującej postaci:
x
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxxxx
xxxxxxxxx
xxxxxxxxxx
Babcia woli jednak przechowywać te wzory w postaci skryptów Pythona zamiast gotowych plików tekstowych ze wzorkiem, bo jak twierdzi "Skrypty zajmują w komputerze mniej bajtów - cokolwiek by to było".
Napisz pętlę while, która wygeneruje taki napis składający się z liter 'x' powielanych wiele razy.
'''

firstRow = 1
lastRow = 31

currentRow = firstRow

while currentRow <= lastRow:
    print("Row number",currentRow)
    currentRow+=1

#################

start = 1
end   = 13

number = start

while number<=end:
    print(number, number*number, number*number*number)
    number+=1

##################

start = 0
end   = 16

x = start

while x<=end:
    print(x, 2**x)
    x+=1

###################   

start = 1
end   = 10

number = start

while number<=end:
    print(number*'x')
    number+=1