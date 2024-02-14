#for number in range(1,21,2): # od ile do ile i o jaki parametr, moze byc tylko jedna liczba (ile)
#    print(number)

for number in range(1,21):
    if number %2 == 0:
        print('Number %2d is %s' % (number,'even')) # even - parzysta
    else:
        print('Number %2d is %s' % (number,'odd')) # odd - nieparzysta

# zadanie

'''
Dane są następujące napisy:
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'
Korzystając z polecenia FOR wyświetl:
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
Korzystając z polecenia FOR wyświetl:
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
Korzystając z polecenia FOR wyświetl:
x
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxxxx
xxxxxxxxx
(wskazówka: aby wyświetlic 5 liter x użyj "x" *5

Korzystając z polecenia FOR wyświetl:
o
xx
ooo
xxxx
ooooo
xxxxxx
ooooooo
xxxxxxxx
ooooooooo
'''

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'
 
for i in range(10):
    print(string_A)
print('')
 
for i in range(9):
    if i % 2 == 0:
        print(string_A)
    else:
        print(string_B)
print('')
 
    
for i in range(1,10):
    print("x"*i)
print('')
 
for i in range(1,10):
    if i % 2 == 0:
        print("x"*i)
    else:
        print("o"*i)