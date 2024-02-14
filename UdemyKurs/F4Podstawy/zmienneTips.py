title = 'Python'
print('Title is', type(title))

Version = 3
print('Version is', type(Version))

Progress = 0.21
print('Progress is', type(Progress))

# typy zmiennych sa silniejsze i slabsze, tu widac ze float jest silniejszy niz int
print('This expresion is', type(Progress * Version))

# kilka zmiennych o tej samej wartosci mozna zainicjowac tak, mozna pozniej zmienic wartosc zmiennej
a = b = c = 2
print(a, b, c)
c = 4
print(a, b, c)

# kolejnosc dzialan zgodnie z matematyka, najpierw nawiasy, potem mnozenie dzielenie (po kolei), potem dodawanie odejmowanie (po kolei)
print(6/2*(1+2))

# UWAGA x++ (zwiekszanie wartosci o 1) W PYTHONIE NIE DZIALA !!!!


# zadania


v1 = 126
v2 = '126'
v3 = 126.0
v4 = '126.0'

print(v1, type(v1))
print(v2, type(v2))
print(v3, type(v3))
print(v4, type(v4))

print(v1+v3, type(v1+v3))
print(v2+v4, type(v2+v4))

print(7-1*0+3+3)

print(4**5/2**3)

print(99+9/9)