for candidate in range(2,31):
    isPrime = True
    for divider in range(2, candidate): # prime number - liczba pierwsza (nie jest podzielna przez mniejsze liczby)
        if candidate % divider == 0:
            isPrime = False
            print('%2d is not a prime number - divider is %2d' % (candidate, divider))
            break
    if isPrime:
        print('%2d is prime!' % (candidate))

# prostsza wersja

for candidate in range(2,31):
    for divider in range(2, candidate): # prime number - liczba pierwsza (nie jest podzielna przez mniejsze liczby)
        if candidate % divider == 0:
            print('%2d is not a prime number - divider is %2d' % (candidate, divider))
            break
    else:
        print('%2d is prime!' % (candidate))


# zadania

'''
ZADANIE 1
Dany jest tekst:
    text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'
Ten tekst to definicja pewnego pojęcia. Twoim zadaniem jest zbudowanie streszczenia tej definicji poprzez wyświetlenie piewszych 20 słów
-podziel ten tekst ze względu na spacje i zapisz wynik w zmiennej words
-zadeklaruj zmienną short_text, która będzie pustym napisem
-zadeklaruj zmienną counter o wartości 0
-dla każdego słowa z listy words
    -dodaj przetwarzane słowo do short_text
    -zwiększ liczbę counter o 1
    -jeżeli liczba counter jest >= 20
        -wyświetl tekst
        -przerwij pętlę

ZADANIE 2
Dana jest lista definicji:
definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'  
    ]
Twoim zadaniem jest zbudowanie streszczeń tych definicji poprzez wyświetlenie tylko pierwszych 20 słów z każdej definicji. Zmień w odpowiedni sposób rozwiązanie zadania 1, tak aby przetwarzana była cała lista
'''

text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'
 
short_text = ''

words = text.split(' ')
counter = 0
 
for word in words:
    short_text += word+' '
    counter += 1
    if counter>=20:
        print(short_text)
        break
    
##################
 
definitions = [
    'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
    'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
    'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
    'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'  
    ]
 
for definition in definitions:
    words = definition.split(' ')
    short_text = ''
    counter = 0
    for word in words:
        short_text += word+' '
        counter += 1
        if counter>=20:
            print(short_text)
            break