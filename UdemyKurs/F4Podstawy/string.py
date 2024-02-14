atext = "This is a text."
print(atext.endswith("ext")) # boolean, sprawdza czy tekst konczy sie na "ext"
print(atext.endswith("ext."))
print(atext.islower()) # Return True if the string is a lowercase string, False otherwise.
print(atext.upper()) #Return a copy of the string converted to uppercase.
print(atext.upper().isupper())

print(atext.find("is"))
print(atext.find("is",3)) # szuka hdzie 'is' od pozycji 3

#print(atext.replace("a", 4)) #TypeError: replace() argument 2 must be str, not int
print(atext.replace("a", "4"))
print(atext.replace("a", "4").replace("i", "1").replace("e", "3"))

print(atext.split(" "))

somethingLikeNumber = "1000"
#somethingLikeNumber + 1 # niedozwolone inne typy zmiennych
print(somethingLikeNumber.isdigit()) # sprawdzenie zmiennej czy mozna przekonwertowac na liczbe

#zadanie

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

print(quote.upper())

print(quote.lower())

print(quote.endswith('street'))

print(quote.isupper())

print(quote.upper().isupper())

print(quote.find('one'))

print(quote.replace('one','1'))

print(quote.replace('one','1').replace('both','2'))

print(quote.split(' '))

print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())