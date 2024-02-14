# konkatenacja czyli laczenie danych

# drive = "c:\"     --- blad bo backslash zmienia info za nim
#   \n  --- new line
#   \a  --- beep (sound)
#   \'  --- just apostrophe
#   \\  --- just backslash

drive = "c:\\"
folder = "scripts\\python\\"
file = "myscript.py"
path = drive + folder + file
print(path)

justText = "text with\nnew line"
print(justText)
justText2 = r"text with\nnew line" # z r(raw) z przodu traktuje jak surowy tekst
print(justText2)

donald = "Mc Donald's" # wersja 'Mc Donald's' z pojedynczym apostrofem blad skladni
print(donald)
donalds = 'Mc Donald\'s' # wersja z backslashem przed apostrofem poprawna
print(donalds)

line = 'He said "I like Python!"' # jak cudzyslow w srodku wtedy apostrof na zewnatrz
print(line)

# zadanie

firstName = 'Kasia'
familyName = 'Sowa'
lastName = 'Mrugala'

newName = firstName+familyName+lastName
print(newName)

newName = firstName+" "+familyName+" "+lastName
print(newName)

music = '"Universal Fanfare" Jerry Goldsmith "Happy Together" Garry Bonner "I\'m a Man" Steve Winwood'
print(music)
# or    
music = "\"Universal Fanfare\" Jerry Goldsmith \"Happy Together\" Garry Bonner \"I'm a Man\" Steve Winwood"
print(music)

music = '"Universal Fanfare" Jerry Goldsmith\n"Happy Together" Garry Bonner\n"I\'m a Man" Steve Winwood\a'
print(music)

print('(\\(\\') 
print('(-.-)') 
print('O_(")(")')