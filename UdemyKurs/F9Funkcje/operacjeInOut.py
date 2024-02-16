# filename = input('Enter filename: ')
# print('The filename is : %s' % (filename))

# wszystko co czyta funkcja input to napis, stad w ponizszym kodzie wyjdzie blad
'''
filesize = input('Enter the max filesize: ')
print('The max filesize is : %d' % (filesize)) # trzeba zaminic %d na %s
'''

filesizeStr = input('Enter the max file size (MB): ')
filesizeInt = int(filesizeStr)

print('The max filesize is : %d' % (filesizeInt))
print('Size in KB is: %d' % (filesizeInt * 1024))

while True:
    filesizeStr2 = input('Enter the max file size (MB): ')
    
    if filesizeStr2.isdecimal():
        filesizeInt2 = int(filesizeStr2)
        break

print('The max filesize is : %d' % (filesizeInt))
print('Size in KB is: %d' % (filesizeInt * 1024))

# zadania
'''
Teraz zajmiemy się rozwiązaniem równania kwadratowego. Te kilka wzorów może się przydać:
    wzory na https://www.udemy.com/course/python-dla-poczatkujacych/learn/lecture/11785556#overview
Przyda się również funkcja, która sprawdzi czy liczba jest całkowita (funkcja isdecimal() niespecjalnie mi się podoba, bo jej zdaniem liczby ujemne np. -1 nie jest liczbą całkowitą):

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

Aby rozwiązać zadanie należy:
    zapytać użytkownika o współczynniki a,b i c
    jeśli a lub b lub c nie są liczbami całkowitymi, to należy wyświetlić odpowiednią informację i zakończyć skrypt
    w przeciwnym razie
        należy sprawdzić czy a == 0
        jeżeli tak, należy wyświetlić informację, że to nie jest równanie kwadratowe i zakończyć skrypt
        w przeciwnym razie
            należy wyliczyć deltę
            jeżeli delta <0, to należy wyświetlić komunikat o braku rozwiązań i zakończyć skrypt
            jeżeli delta=0,  to należy wyliczyć x1, wyświetlić wynik i zakończyć skrypt
            jeżeli delta>0, to należy wyliczyć x1 i x2 , wyświetlić wynik i zakończyć skrypt
Po napisaniu skryptu przetestuj go z różnym danymi testowymi, np dla a, b i c:
    3, 4, 1 - 2 rozwiązania:  -1 i -0.33
    5, 4, -1 - 2 rozwiązania: -1 i 0.2
    5, 4, 1 - brak rozwiązań
    2, 0, 0 - jedno rozwiązanie: 0
    0, 3, 4 - komunikat o tym, że a == 0
    one, 1,1 - komunikat o tym, że a, b i c muszą być liczbami całkowitymi
'''

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
 
print('This program solves equation ax^2+bx+c = 0')
print('Enter the values for a, b and c:')
 
a_str = input('a=')
b_str = input('b=')
c_str = input('c=')
 
if not( check_int(a_str) and check_int(b_str) and check_int(c_str) ):
    print("a, b and c need to be int!")
else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
 
    if a == 0:
        print('a cannot be 0!')
    else:
        delta = b**2 - 4*a*c
 
        if delta < 0:
            print("there is no solution")
        elif delta == 0:
            x1 = -b/(2*a)
            print("there is one solution: %.2f" % (x1))
        else:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print("there are two solutions: %.2f and %.2f" % (x1,x2))