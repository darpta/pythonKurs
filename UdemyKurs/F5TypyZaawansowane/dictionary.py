CountryLeaders = {'PL':'Duda','US':'Biden'} # utworzenie slownika poprzez dodanie wartosci klucz + wartosc

print(CountryLeaders['US']) # wyswietlenie wartosci

CountryLeaders['DE'] = 'Merkel' # dodawanie klucza i wartosci do slownika

#print(CountryLeaders.keys()) # wyswietla klucze
#print(CountryLeaders.values()) # wyswietla wartosci
#print(CountryLeaders.items()) # wyswietla kolekcje (klucz + wartosc)

#print(CountryLeaders.popitem()) # destrukcyjna iteracja, przechodzi przez slownik i tez usuwa element po elemencie

#print(CountryLeaders.get('RU')) # szuka wartosci, nie ma w slowniku, wiec wynik None
#print(CountryLeaders.setdefault('FR','Macron')) # szuka, jak nie ma to dodaje do slownika

print(CountryLeaders)

NewLeaders = {'RU':'Putin','DE':'Schulz'}
print(NewLeaders)

CountryLeaders.update(NewLeaders) # zmiana istniejacych wartosci lub dodanie nieistniejacych

print(CountryLeaders)

# zadania

'''
Nadal analizujesz wydajność kanałów, jakimi można dotrzeć do klientów. Każdorazowo po zmienie słownika wyświetl jego zawartość
1. Utwórz obiekt dictionary o nazwie chanels z następującymi kluczami i wartościami:
-Google - 1480
-Email - 300
-Natural Traffic - 440
-TV Spot - 700
2. Wyświetl wartość skojarzoną z kluczem "Email"
3. Utwórz nowy słownik chanelsUpdate z kluczami i wartościami:
-Natural Traffic -  520
-News - 600
4.Zaktualizuj słownik chanels wartościami z chanelsUpdate
5. Wyświetl wszystkie klucze z chanels
6. Usuń wartość 'Email' ze słownika
'''

chanels={'Google':1480,'Email':300,'Natural Traffic':440,'TV Spot':700}
print (chanels)
print(chanels['Email'])
chanelsUpdate={'Natural Traffic':520,'News':600}
chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
print(chanels.pop('Email'))
print(chanels)