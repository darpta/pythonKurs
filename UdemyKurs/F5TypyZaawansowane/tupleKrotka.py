Tax = (4, 7, 8, 23)

print(Tax[2])
print(Tax[-1]) # odniesienie od konca, nie ma wtedy zera, -1 jest pierwsze
print(Tax.index(7)) # podaje index wartosci 7
print(Tax.count(8)) # zlicza wystapienia wartosci 8
print(max(Tax)) # podaje najwyzsza wartosc w krotce

TaxList = list(Tax) # aby zmienic wartosci trzeba tuple przekonwertowac na liste

TaxList.append(30) # dodanie wartosci do listy
NewTax = tuple(TaxList) # zamiana listy na tuple

print(Tax)
print(TaxList)
print(NewTax)

(tax1, tax2, tax3, tax4) = Tax # utworzenie czterech zmiennych i przypisanie im wartosci z tuple
print(tax1, tax2, tax3, tax4)

a = 1
b = 10
print('a =',a,'\tb =',b)#

#temp = a --- trzeba dodac tymczasowa zmienna zeby zamienic wartosci zmiennych
#a = b
#b = temp
(a,b) = (b,a) # zamiana z uzyciem tuple nie wymaga tymczasowj zmiennej
print('a =',a,'\tb =',b)

# zadania

'''
Przygotowujesz się do analizy email-marketingu. Po każdym zadaniu poniżej wyświetl listę:
1. Utwórz listę o nazwie marketing z elementami:
-loyality program
-client promotion
-market research
2. Dodaj do listy element 'public relations'
3. Wyświetl pozycję numer 3
4. Wstaw na pozycję numer 2 element 'investor relations'
5. Chcesz jednak aby lista znajdowała się w zmiennej o nazwie emailMarketing. Skopiuj elementy z listy marketing do listy emailMarketing
6. Posortuj listę emailMarketing
7. Utwórz nową jednoelementową listę internalEmails. Jedyny element to 'internal communication'
8. Dodaj listę internalEmails do listy emailMarketing
9. Utwórz tuple, którego wartości pochodzą z listy emailMarketing. Podczas wyświetlania tuple zwróć uwagę na nawiasy, z jakich skorzystał Python
'''

marketing=['loyality program','client promotion','market research']
print(marketing)
marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2,'investor relations')
print(marketing)
emailMarketing = marketing.copy()
print(emailMarketing)
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal comunication']
emailMarketing.extend(internalEmails)
print(emailMarketing)
emailTuple = tuple(emailMarketing)
print(emailTuple)