'''
Zaczynamy od programu stworzonego w poprzednim przykładzie. Zamiast opcji "pokój" oprogramujemy opcję "wojna". Jeżeli obaj gracze mają taką samą kartę, to:
    wykładają jeszcze jedną kartę, która o niczym nie decyduje
    wykładają kolejną kartę i w zależności czyja karta jest większa, ten gracz zgarnia wyłożone karty
    gdyby jednak karty nadal miały tą samą moc to powtarzamy wyżej opisaną sekwencję
    gdyby w czasie wojny któremuś z graczy skończyły się karty, to ten gracz przegrywa
Poniżej propozycja rozwiązania ktok po kroku:
1. Gdzieś trzeba zapamiętać jakie karty są obecnie wyłożone. Dlatego zaraz po pobraniu kart w pętli while utwórz pustą listę o nazwie stock
2. Teraz zupełnie możesz wykasować zawartość pierwszego wyrażenia if, bo tu wszystko się zmieni
3. Ponieważ wojna może się składać z kilku ruchów napisz pętlę while, która będzie działać tak długo, jak długo moc card1 i card2 są sobie równe.
    w tej pętli wyświetl informację o tym, że toczy się wojna i jaką moc mają obie karty
    dodaj obie karty do listy stock
    Teraz sprawdzimy, czy któremuś z graczy nie skończyły się karty:
        Jeżeli gracz 1 ma mniej niż 2 karty, to
            wszystkie karty ze stock należy dopisać do player2
            wszystkie karty z player1 należy dopisać do player2
            lista player1 ma się stać pusta
            wewnętrzną pętlę można przerwać poleceniem break
        W przeciwnym razie, jeżeli gracz 2 ma mniej niż 2 karty, to:
            wszystkie karty ze stock należy dopisać do player1
            wszystkie karty z player2 należy dopisać do player1
            lista player2 ma się stać pusta
        W przeciwnym razie, czyli kiedy obaj gracze mają wystarczającą ilość kart:
            należy do card1 pobrać kolejną kartę z player1
            należy do card2 pobrać kolejną kartę z player2 (to te karty, które kładzie się na stosie, ale króre niczego nie zmieniają)
            obie karty należy dopisać do listy stock
            należy do card1 pobrać kolejna kartę z player1
            należy do card2 pobrać kolejną kartę z player2 (to nowe decydujące o losach wojny karty)
    W przeciwnym razie do warunku while, czyli gdy karty nie są równe: (****)
        Jeśli card1 jest mocniejsza niż card2
            do stock dodaj card1 i card2
            dopisz do player1 zawartość stock
        W przeciwnym razie
            do stock dodaj card1 i card2
            dopis do player2 zawartość stock
4. Możesz jeszcze w krytycznych miejscach dodać komunikaty o toczącej się wojnie i ewentulanych wygranych, przegranych i remisach. Będzie to przydatne jeśli coś idzie nie tak i trzeba będzie zrozumieć decyzje programu
5. Uruchom program. Jeśli wszystko poszło dobrze, teraz rozgrywki powinny się kończyć szybciej
----------------------
(****)  zauważ jak ładnie można tu skorzystać z else uruchamianego dla while. Polecenie break wykonywane w przypadku braku kart u któregoś z graczy pomija ten blok else i właściwie od razu przeskakujemy do pętli zewnętrznej, która sprawdza, czy któryś z graczy nie został już bez kart. Jeśli jednak pętla przerwie się z powodu różnych kart na stosie, to wtedy blok else się wykona i po prostu oddamy karty ze stosu jednemu z graczy.

Możesz przestudiować działanie tego kodu, z włączonym lub wyłączonym komentarzem:

i=0
 
while i < 10:
    print(i)
   # if i == 3:
    #    break
    i+=1
else:
    print('else')
 
print('end')
'''

# zadanie

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]
 
allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)
 
import random
 
random.shuffle(allCards)
print(allCards)
 
player1 = []
player2 = []
 
player1 = allCards[:12]
player2 = allCards[12:]
 
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 1--------')
print(player2)    
 
while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
 
    stack = []  
 
    if card1["Power"] == card2["Power"]:
        while card1["Power"] == card2["Power"]:
 
            print('WAR',card1['Power'],card2['Power'])
            stack.append(card1)
            stack.append(card2)
 
            if len(player1)<2:
                player2.extend(stack)    
                player2.extend(player1)
                player1 = []
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
                break
            elif len(player2)<2:
                player1.extend(stack)    
                player1.extend(player2)
                player2 = []
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stack.append(card1)
                stack.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        else:
            if card1["Power"] > card2["Power"]:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
            
 
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        #print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1)*'*')
    else:
        player2.append(card2)
        player2.append(card1)
        #print('PLAY-2 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2)*'*')
 
if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')