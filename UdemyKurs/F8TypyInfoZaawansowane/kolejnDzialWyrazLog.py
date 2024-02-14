'''
Zapisz swój numer buta i pomnóż przez 5. Do tego dodaj 50.
Całość pomnóż przez 20, a następnie dodaj 1017. Odejmij od tego swój rok urodzenia.
Wyszła 4cyfrowa liczba. Pierwsze dwie cyfry to Twój numer buta a dwie ostatnie to Twój wiek.
'''
shoesize = 45
number = (shoesize*5 +50)*20+1017 -1973
print('shoe size is:',number //100)
print('birth date is:',number %100)
'''
Pomyśl liczbe nieujemną całkowitą. Pomnóż ją przez 2, dodaj 10, podziel przez 2, odejmnij początkową liczbę.
Powinno wyjść 5 - zawsze.
'''
x=107
print('this should be 5:',(x*2+10)/2-x)
print('2+2*2=',2+2*2)
print('7+7/7+7*7-7',7+7/7+7*7-7)
presence = 0.85
note =3.5
finalWorkOK = False
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)
presence = 0.4
note =2.5
finalWorkOK = True
print('you need to be present and have good notes or do the final work',presence >=0.8 and note >=3 or finalWorkOK)
print('you need to be present and have good notes and do the final work',presence >=0.8 and note >=3 and finalWorkOK)