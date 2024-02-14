cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()

print(cargo)

boxCapacity = 90
box = []
i = 0

while i < len(cargo) and boxCapacity - sum(box) >= min(cargo):
    if boxCapacity - sum(box) >= cargo[i]:
        box.append(cargo[i])
    i+=1



print('The collected items sum is:',sum(box))
print('The elements are:', box)


# zadania

'''
1. Dokuczałeś prowadzącemu ten kurs i dostajesz "za karę zadanie" - musisz wyznaczyć sumy dwóch kolejnych liczb od 0 do 50, np
0+1 = 1
1+2 = 3
2+3 = 5
3+4 = 7 itd.
Wyjmij kartkę i licz lub:
- zadeklaruj zmienną number i przypisz jej wartość 1
- zadeklaruj zmienną previousNumber i przypisz jej wartość 0
- napisz  pętlę while, która wykonywać się będzie tak długo, jak długo number jest mniejsze niż 50
- w pętli:
    - wyświetl sumę number i previous_number
    - do previous_number przypisz wartość number
    - zwiększ number o 1

2. Teraz napiszesz... poniekąd prostą grę. Zasady są proste. Komputer wymyśli sobie liczbę od 0 do 20, a Ty musisz ją zgadnąć!
Polecenia
import random
my_number = random.randint(0,20)
wygenerują liczbę losową i umieszczą jej wartość w zmiennej my_number (więcej o module random w dalszej częśći kursu).
Zadeklaruj zmienną guess i przypisz jej wartość -1 (to wartość spoza zakresu losowanych liczb - czyli na pewno nie jest równa wylosowanej liczbie)
Wyświetl instrukcję do gry - przynajmniej słowa "Guess my number!"
Wykonuj pętlę while tak długo jak wartość w zmiennej guess jest różna od wartości my_number
poleceniem
guess = int(input())
wczytaj odpowiedź użytkownika (uwaga program nie jest odporny na wprowadzenie w tym miejscu np. napisu zamiast liczby - o obsłudze błędów opowiadam w ostatnim module kursu)
Sprawdź wartość liczby guess i
- jeżeli jest równa my_number, to wyświetl gratulacje
- w przeciwnym razie jeśli guess jest większe od my_number wyświetl "Sorry- my number is smaller than your guess, Try again!"
- w przeciwnym razie wyświetl  "Sorry- my number is greater than your guess, Try again!"
A teraz pobaw się kilka razy ;)

3. Do poprzedniego zadania dodaj zmienną trials, która będzie liczyć ilość prób. Początkowo powinna mieć wartość 0, a potem po każdej instrukcji wczytywania liczby guess ma być powiększana o 1.
Wyświetlając gratulacja wyświetl też informacje za którym razem udało się odgadnąć liczbę
'''

number = 1
previous_number = 0
 
while number<=50:
    print(number + previous_number)
    previous_number=number
    number+=1
 
#############################
 
import random
my_number = random.randint(0,20)
guess=-1
 
print("Guess my number!")
 
while guess != my_number :
 
    guess = int(input())
    
    if guess == my_number:
        print("You are right! It was:",my_number)
    elif guess>my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")
 
##########################
 
import random
my_number = random.randint(0,20)
guess=-1
trials = 0
 
print("Guess my number!")
 
while guess != my_number :
 
    guess = int(input())
    trials+=1
    
    if guess == my_number:
        print("You are right! It was:",my_number,"You needed",trials,"trials.")
    elif guess>my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")