f_smaller = 3.141592653589793
f_bigger = 3.87756392764

import math

print(math.ceil(f_smaller), math.ceil(f_bigger))    # zwraca najmniejsza liczbe calkowita, ktora jest wieksza od danej
print('\n')

print(math.floor(f_smaller), math.floor(f_bigger))  # zwraca najwieksza liczbe calkowita, ktora jest mniejsza od danej
print('\n')

print(math.ceil(-f_smaller), math.ceil(-f_bigger))  # Uwaga! dla liczb ujemnych jest odwrotnie
print('\n')

print(math.floor(-f_smaller), math.floor(-f_bigger))    # Uwaga! dla liczb ujemnych jest odwrotnie
print('\n')

print(pow(2,8), pow(9,0.5)) # funkcja power, liczba ktora chcemy podnosic + do jakiej potegi; pow(9,0.5) to pierwiastek z 9 (inaczej 9 do potegi jedna druga)
print('\n')

print(math.sqrt(16)) # zwraca pierwiastek kwadratowy z 16
print('\n')

print(math.pi, math.e)
print('\n')

print(math.sin(math.pi/2), math.cos(math.pi/4)) # funkcje trygonometryczne
print('\n')


# zadania

'''
1. Zaimportuj moduł math (zrobione wczesniej)

2. Oto wzory pozwalające na wykonanie konwersji stopni na radiany i radianów na stopnie:
    1° = (π * rad)/180   
    1 rad = 180°/π   
3. Zadeklaruj zmienną degree i przypisz jej wartość 360. Wylicz i wyświetl ile wynosi wartość radianów dla 360 stopni

4. Zmień wartość zmiennej degree na 45 stopni i powtórz obliczenia

5. ... ale moduł math ma funkcję radians, która wykonuje konwersję stopni na radiany! Porównaj wyniki zwracane przez Twoje obliczenia z obliczeniami funkcji radians.

6. Pizzeria oferuje pizze:
    small - promień 22 cm, cena, 11.50
    big - promień 27 cm, cena 15.60
    family - promień 38cm, cena 22.00
Zadeklaruj zmienne small_pizza_r, big_pizza_r, family_pizza_r oraz small_pizza_price, big_pizza_price, family_pizza_price i zapisz w nich w/w wartości.

7. Oblicz pole powierzchni pizz w metrach kwadratowych
8. Wyznacz cenę metra kwadratowego pizzy small, big i family
9. Zobacz jakie inne funkcje są dostępne w module math. Możesz w tym celu odwiedzić stronę
https://docs.python.org/2/library/math.html
lub wykonać polecenie:
math_ls = dir(math) 
print(math_ls)
'''

degree = 360
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
 
degree = 45
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
print('')
 
print("%d degree is %f radians" % (360, math.radians(360)))
print("%d degree is %f radians" % (45, math.radians(45)))
print('')
      
small_pizza_r = 0.22
big_pizza_r = 0.27
family_pizza_r = 0.38
 
small_pizza_price = 11.50
big_pizza_price = 15.60
family_pizza_price = 22.00
 
small_area = math.pi * small_pizza_r**2
big_area = math.pi * big_pizza_r**2
family_area = math.pi * family_pizza_r**2
 
print('small', small_pizza_r,small_pizza_price, small_area)
print('big', big_pizza_r,big_pizza_price, big_area)
print('family', family_pizza_r,family_pizza_price, family_area)      
print('')
print('small', small_pizza_price/small_area)
print('big', big_pizza_price/big_area)
print('family', family_pizza_price/family_area)
print('')
      
math_ls = dir(math) 
print(math_ls)