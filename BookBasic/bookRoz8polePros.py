import sys

print("Program obliczajacy pole prostokata")
a = int(input("Podaj dlugosc boku a: "))
b = int(input("Podaj dlugosc boku b: "))

if(a <= 0 or b<= 0):
    print("Dlugosc boku nie moze byc ujemna!")
    sys.exit()

pole = a * b
if(pole != 13):
    print("Dobrze, ze nie 13, bo 13 jest pechowe!")
print(pole)