import sys

def dodawanie(a, b):    # def oznacza funkcje
    return a + b        # skrocona wersja zapisu wersji rozbudowanej
''' wersja rozbudowana:
    c = a + b
    return c
'''
def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

def zlyWybor():
    print("Dokonales zlego wyboru!")
    sys.exit()

a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
c = input("Wybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie: ")

if(c == '1'):
    wynik = dodawanie(a, b)
elif(c == '2'):
    wynik = odejmowanie(a, b)
elif(c == '3'):
    if(b == 0):
        print("Nie wolno mnozyc przez 0")
        sys.exit()
        #exit()
    else:
        wynik = mnozenie(a, b)
elif(c == '4'):
    if(b == 0):
        print("Nie wolno dzielic przez 0")
        sys.exit()
        #exit()
    else:
        wynik = dzielenie(a, b)
else:
    zlyWybor()

print("Wynik dzialania to: ", wynik)