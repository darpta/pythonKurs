def GiveWorkingDay():
    # prints the nearest working day date
    
    from datetime import date
    from datetime import timedelta

    # day = date.today()
    day = date(2017,10,1)

    if day.weekday() == 5: # sobota bo index 6
        workingday = day + timedelta(days=2) # aby uzyskac dzien roboczy trzeba dodac 2 dni
    elif day.weekday() == 6: # niedziela bo index 7
        workingday = day + timedelta(days=2) # aby uzyskac dzien roboczy trzeba dodac 1 dzien
    else:
        workingday = day
        
    print('working day for',day,'is',workingday)

    return

GiveWorkingDay()

# zadanie
'''
Przygotujmy funkcję, która wyświetli ile dni zostało do końca roku. Jeśli wiesz jak to zrobić to nie czytaj dalej, a jeśli chcesz pewnych wskazówek - oto one:
    najpierw napisz skrypt, potem skonwertujesz go do funkcji
    zaimportuj z modułu datetime typ date
    korzystając z funkcji today() z modułu date zapisz w zmiennej date_today datę dzisiejszą
    korzystając z odpowiedniej właściwości zmiennej date_today pobierz rok z tej daty do zmiennej current_year
    do zmiennej date_end_year zapisz datę zbudowaną z current_year, 12 (grudzień) i 31 (Sylwester). Skorzystaj z metody date, do której przekażesz te zmienne
    do zmiennej delta zapisz różnicę między date_end_year i date_today
    wyświetl ilość dni z obiektu delta. Skorzystaj z odpowiedniej właściwości
    sprawdź działanie skryptu
    skonwertuj skrypt na funkcję
    sprawdź działanie funkcji wywołując ją
No to dużo jeszcze do Sylwestra?
'''

def DaysToEndOfYear():
    # prints how many days till the end of year
    from datetime import date
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print('Days to the end of year: ',delta.days)
 
DaysToEndOfYear()