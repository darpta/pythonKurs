'''
ZADANIE 1
Ciąg Fibonacciego to ciąg rozpoczynający się od 0 i 1 a każda kolejna liczba to suma dwóch poprzednich, np:
0
1
0+1 = 1
1+1 = 2
1+2 = 3
2+3 = 5
....
Korzystając z pętli for napisz program, który wyliczy fibonacciIterations=20 pierwszych elementów ciągu Fibonacciego
Wskazówka:
-zadeklaruj 3 dodatkowe zmienne a1, a2 i a3. Początkowo a1=0 a a2=1. a3 będziesz wyliczać jako sumę a1 i a2. W pętli trzeba też będzie zmieniać wartość a1 na a2 oraz a2 na a3

ZADANIE 2
Masz dany tekst:
    Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was found that this solution just couldn't do the job. Python was compared to other languages, such as Tcl and Perl, and chosen because it's an easier-to-learn language that the organization can implement incrementally. In addition, Python can be embedded within a larger software system as a scripting language, even if the system is written in a language such as C/C++. It turns out that Python can successfully interact with these other languages in situations in which some languages can't.
Twoim zadaniem jest wyświetlić tylko te słowa, które zawierają literkę "p"

ZADANIE 3
Dany masz słownik:
dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less than 50%'} 
Wyświetl zestawienie w postaci (kolejność nie jest istotna):
A - 80%-100%
B - 60%-80%
C - 50-60%
D - less than 50%

ZADANIE 4
Należy policzyć ile razy w w/w tekście występowały poszczególne słowa
Wskazówki:
-zadeklaruj zmienną wordDictionary typu dictionary. Obiekt na początku ma być pusty więc do jego zainicjowania możesz skorzystać z {}. W tym dictionary kluczem będzie słowo z tekstu a wartością ilość wystąpień słowa w tekście
-korzystając z funkcji split(' ') podziel napis na słowa i zaopamietaj w tablicy listOfWords
-dla każdego słowa z tej listy (pętla FOR)
-jeżeli słowo już jest na liście wordictionary.keys() - to do value dodaj 1 
-jeżeli słowo nie występowało jeszcze na liście to dodaj je jako nowy element dictionary z kluczem równym słowu i wartością 1 (można skorzystać np z funkcji  
    setdefault 
lub notacji 
    wordDictionary[word]=1
'''

fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0
for i in range(0,20):
    print('Step',i,'value',a3)
    a1=a2
    a2=a3
    a3=a1+a2

######################### 
 
text='''
Industrial Light & Magic: In this case, you find Python used in the production process for scripting complex, computer graphic-intensive films. Originally, Industrial Light & Magic relied on Unix shell scripting, but it was found that this solution just couldn't do the job. Python was compared to other languages, such as Tcl and Perl, and chosen because it's an easier-to-learn language that the organization can implement incrementally. In addition, Python can be embedded within a larger software system as a scripting language, even if the system is written in a language such as C/C++. It turns out that Python can successfully interact with these other languages in situations in which some languages can't.
'''
listOfWords = text.replace("\n"," ").split(' ')
for word in listOfWords:
    if word.lower().find('p')>=0:
        print(word)

######################### 
 
dictionary={'A':'80%-10%','B':'60%-80%','C':'50-60%','D':'less than 50%'}
for word in dictionary.keys():
    print(word,'-',dictionary[word])

######################### 

# listOfWrods z zadania nr 2
wordDictionary={}
for word in listOfWords:
    if word in wordDictionary.keys():
        wordDictionary[word] = wordDictionary[word]+1
    else:
        wordDictionary.setdefault(word,1)
print(wordDictionary)