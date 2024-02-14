'''
W tym zadaniu zajmiemy się tasowaniem kart. Kto jako dziecko lubił tasować karty? Bo ja nie :) Wybierz sobie język w jakim wykonasz to zadanie, albo... zrób je po polsku :)


1. Zadeklaruj zmienne opisujące figury kart i kolory:
colors = ['Serca','Poduszki','Zoledzie','Wino']
figures = ['As','Krol','Dama','Jupek','10','9']

2. Zadeklaruj zmienną allCards jako pustą listę

3. Napisz zagnieżdżoną pętlę, która przechodzi przez colors i figures i dodaje do allCards napis będący połączniem nazwy koloru i figury

4. Wyświetl allCards - zauważ, że porządek kart jest wg kolorów i figur

5. Zaimportuj moduł random

6. Wymieszaj karty znajdujące się w zmiennej allCards. Wyświetl potasowane karty

7. Pora rozdać karty graczom. Zrobimy to na 2 sposoby. Ale najpierw zadeklaruj puste listy player1 i player2

8. Sposób pierwszy:
Do zmiennej max przypisz wartość określającą długość listy allCards
Napisz pętlę sterowaną przez zmienną i zmieniającą się od zera do max-1, a w tej pętli:
jeżeli i jest parzyste - dodaj element allCards[i] do listy player1
jeżeli i jest nieparzyste - dodaj element allCards[i] do listy player2
Wyświetl karty gracza 1 i 2

9. Sposób drugi - poprzednie rozwiązanie nawiązuje do tego w jaki sposób rozdajemy karty do gry. Ale skoro karty i tak są wymieszane to w przypadku 24 kart można by pierwszych 12 dać pierwszemu graczowi, a pozostałe 12 drugiemu. Dlatego: nie korzystając z pętli:
przepisz do player1 elementy z allCards od 0 do 11
przepisz do player2 elementy z allCards od 12 do 23
wyświetl karty obu graczy
'''

colors = ['Serca','Poduszki','Zoledzie','Wino']
figures = ['As','Krol','Dama','Jupek','10','9']
 
allCards = []
for c in colors:
    for f in figures:
        allCards.append("%s - %s" % (c, f))
 
print(allCards)
 
import random
 
random.shuffle(allCards)
print(allCards)
 
player1 = []
player2 = []
 
max = len(allCards)
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 2--------')
print(player2)              
 
player1 = allCards[:12]
player2 = allCards[12:]
 
 
print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 2--------')
print(player2)