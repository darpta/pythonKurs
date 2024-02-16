'''
Budujemy moduł służący do obliczeń na ciągach geometrycznych

ZADANIE 1
Zaimportuj moduł math
Przygotuj funkcję GiveGeomSeqElement, która:
-przyjmuje 3 parametry a1 - o domyślnej wartości  2, która oznacza pierwszy element ciągu, factor - o domyślnej wartości 2, która oznacza iloraz ciągu geometrycznego, index o domyślnej wartości 2, która oznacza  który element ciągu ma być wyliczony
-dodaj do funkcji komentarz, który opisze co robi ta funkcja
-wylicz wartość ciągu. Odpowiedni wzór znajdziesz np tu: https://pl.wikipedia.org/wiki/Ci%C4%85g_geometryczny
Wylicz wartość 64 elementu ciągu geometrycznego, którego pierwszym elementem jest 1 a iloraz wynosi 2

ZADANIE 2
Przetestuj działanie funkcji. Napisz pętlę for, która wyznaczy i wyświetli elementy a1, a2, a3,...a10 dla ciągu geometrycznego o pierwszym wyrazie równym 3 i ilorazie 2

Wskazówki:
-zadeklaruj a1=3, factor=2 i maxindex=10
-napisz pętlę for, gdzie wartość sterująca pętli nazywa się i i zmienia się od 1 do maxindex
-dla każdej wartości wyliczy wartość elementu korzystając z funkcji 

ZADANIE 3
Przygotuj funkcje GiveFactorForGeomSeq, która wyznaczy wartość ilorazu gdy znane są 2 kolejne wyrazy ciągu.
Wskazówki:
-Funkcja ma mieć 2 parametry term i nextterm bez wartości domyślnej
-dodaj komentarz o funkcji
-Aby uzyskać wartość podziel nextterm przez term i zwróć wynik
Przetestuj działanie funkcji dla 12 i 24

ZADANIE 4

Utwórz funkcję GiveSumOfNElementsGeomSeq, która wyznaczy sumę pierwszych wyrazów ciągu.
Funkcja ma:
-przyjąć parametr a1 o domyślnej wartości 2, która oznacza pierwszy wyraz ciągu, factor o domyślnej wartości 2, która oznacza iloraz ciągu i n oznaczające ile pierwszych elementów ciągu ma być dodanych. Domyślna wartość tego praramertu to 2
-wzór na sumę znajdziesz pod adresem: https://pl.wikipedia.org/wiki/Ci%C4%85g_geometryczny
Przetestuj działanie funkcji wyliczając sumę dla ciągu o pierwszym elemencie równym 2, ilorazem 3 dla pierwszych 4 elementów

ZADANIE 5
Przenieś wszystkie funkcje i linijkę importującą moduł math do nowego pliku. Zapisz go pod nazwą geom.py
W pliku skryptu zaimportuj  moduł geom
Zmień instrukcje wywołujące funkcje, aby korzystały z funkcji modułu (dodaj prefix geom. )
Uruchom skrypt i przetestuj funkcje, które zostaną zaimportowane z modułu geom.
'''

# zadania 1-4

import math

def GiveGeomSeqElement(a1=2,factor=2,index=2):
    #returns n-th term of geometric sequence starting with element a1 and having 
    value = a1*pow(factor,index-1)
    return value
print('element 64 =',GiveGeomSeqElement(1,2,64))
print('------------------------------------------------')
a1=3
factor=2
maxindex=10
for i in range(1,maxindex):
    an = GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)
print('------------------------------------------------')
def GiveFactorForGeomSeq(term, nextterm):
    #returns factor for geometrical sequence having two following terms of the sequence
    return nextterm/term
print('Factor is', GiveFactorForGeomSeq(12,24))
print('------------------------------------------------')
def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    #returns sum of n first elements of geometrical sequence with first term a1 and factor
    sumN = a1*(1-pow(factor,n))/(1-factor)
    return sumN
print('Sum of n elements is', GiveSumOfNElementsGeomSeq(2,3,4))


# zadanie 5

# import z pliku geom.py
import geom

print('2^64 =',geom.GiveGeomSeqElement(1,2,64))
print('------------------------------------------------')
a1=3
factor=2
maxindex=11
for i in range(1,maxindex+1):
    an = geom.GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)
print('------------------------------------------------')
print('Factor is', geom.GiveFactorForGeomSeq(12,24))
print('------------------------------------------------')
print('Sum of n elements is', geom.GiveSumOfNElementsGeomSeq(2,3,4))