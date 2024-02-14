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
1. Pamiętasz zadanie "za karę" dodające kolejne liczby?
Oto propozycja rozwiązania. Skopiuj ją do własnego skryptu i uruchom:
number = 1
previus_number = 0
while number<50:
    print(number + previus_number)
    previus_number=number
    number+1
opsss.... zawiesiło się? Skrypt można przerwać naciskając CTRL+C. Korzystając z debuggera znajdź błąd (znajdź go nawet jeśli już widzisz co jest nie tak ;))
W odpowiedziach znajdziesz opis przyczyny problemu

2. Poniższy program ma za zadanie (w nieco dziwny sposób!) utworzyć napis o długości 10 znaków zapisany w zmiennej text. Niestety coś poszło nie tak. Korzystając z debuggera znajdź przyczynę. W odpowiedziach znajdziesz poprawną wersję skryptu z komentarzem
text = ''
number = 10
condition = True
while condition: 
    text+='x'
    print(text)    
if len(text)>number:
    condition=False
'''

# ad 1 --- zapis number+1 jest zly, brakuje 'number=' lub powinno byc number+=1
number = 1
previus_number = 0
 
while number<50:
    print(number + previus_number)
    previus_number=number
    number = number+1

# ad 2 --- brak wciecia if...
text = ''
number = 10
condition = True
while condition: 
    text+='x'
    print(text)    
    if len(text)>number:
        condition=False