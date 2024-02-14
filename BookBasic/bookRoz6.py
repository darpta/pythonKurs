import sys

print("Witaj w prostym kalkulatorze")
a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
'''
if(b == 0):
        print("Nie wolno mnozyc przez 0")
        sys.exit()
'''
# moze byc jak wyzej lub jak w dalszej czesci
c = int(input("Wybierz rodzaj dzialania: 1 - dodawanie, 2 - odejmowanie, 3 - mnozenie, 4 - dzielenie: "))
if(c == 1):
    wynik = a + b
elif(c == 2):
    wynik = a - b
elif(c == 3):
    if(b == 0):
        print("Nie wolno mnozyc przez 0")
        sys.exit()
        #exit()
    else:
        wynik = a * b
elif(c == 4):
    wynik = a / b
else:
    print("Dokonales zlego wyboru!")

d = input("Jesli chcesz otrzymac liczbe calkowita, wybierz 1, przeciwnie wybierz 2: ")
if(d == "1"):
    int(wynik)
    #print(int(wynik))
elif(d == "2"):
    float(wynik)
    #print(float(wynik))

print("Wynik dzialania to: ", wynik)