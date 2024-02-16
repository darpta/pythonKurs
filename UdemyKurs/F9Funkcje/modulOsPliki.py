import os
import time

# czynnosci ze sciezkami do plikow

print('Current directory is:',os.getcwd())

currentDir = os.getcwd()
filename = 'results.txt'
fullpath = os.path.join(currentDir,filename)
print('\nThe constructed file path is: ',fullpath)

relativepath = 'output.txt'
print('\nThe absolute path is: ',os.path.abspath(relativepath))

filepath = r'c:\Users\dariu\Python\pythonKurs\results.txt'   # r = raw string - nie potrzeba podwojnego backslasha
#filepath2 = 'c:\\Users\\dariu\\Python\\pythonKurs\\results.txt'    # taki zapis bez r
print('\nThe file name part is: ',os.path.basename(filepath))
print('The directory part is: ',os.path.dirname(filepath))

print('\nIs file existing? ',os.path.exists(filepath))

if os.path.exists(filepath):
    print('\nLast modifydate is:',os.path.getmtime(filepath))
    print('Last modifydate is:',time.localtime(os.path.getmtime(filepath)))
    
    print('\nFile size is: ',os.path.getsize(filepath))
    
    print('\nIs it a file?',os.path.isfile(filepath))
    print('Is it a dir?',os.path.isdir(filepath))
    
    print('\nPath splitted:',os.path.split(filepath)) # zwraca tuple
    print('Only file name part:',os.path.split(filepath)[1]) # odnosi sie do indeksu 1 z tuple
    
    print('\nPath splitted into drive:',os.path.splitdrive(filepath))
    print('Only drive:',os.path.splitdrive(filepath)[0])


# zadania
'''
1. Zaimportuj moduły os i time

2. Poproś użytkownika o wprowadzenie ścieżki dostępu do katalogu i zapisz pobrany napis w zmiennej dir

3. Jeśli wprowadzony napis nie wskazuje na katalog, wyświetl komunikat i zakończ skrypt

4. W przeciwnym razie poproś użytkownika o wprowadzenie nazwy pliku i zapisz pobrany napis w zmiennej file

5. Korzystając z odpowiedniej funkcji modułu os połącz ze sobą katalog z plikiem tworząc pełną ścieżkę. Wynik zapamiętaj w zmiennej path

6. Jeżeli plik wskazywany przez path nie istnieje, wyświetl komunikat i zakończ skrypt

7. Wyświetl informację o tym, że poniżej będą wyświetlane właściwości pliku path, a potem wyświetl:
    datę ostatniej modyfikacji
    rozmiar w bajtach
    informację o bieżącym katalogu
    ścieżkę względną do pliku
'''

import os
import time
 
dir = input('enter directory name: ')
 
if not os.path.isdir(dir):
    print("%s must be a directory" % dir)
else:
 
    file = input('enter filename saved in directory %s: ' % dir)
 
    path = os.path.join(dir, file)
 
    if not os.path.isfile(path):
        print('File %s does not exist!' % path)
 
    else: 
        print('displaying properties of file %s' % path)
 
        print('Last modified date', time.localtime(os.path.getmtime(path)))
        print('Size in bytes', os.path.getsize(path))
 
        print('Current directory is: ', os.getcwd())
        # print('Relative path to the file is', os.path.relpath(path))      # nie dziala