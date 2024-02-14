message1 = 'Processing file %s' # %s pozwala dodac tekst do wiadomosci
print(message1 % ('file_1.txt'))

message2 = 'File %s has size %d KB' # %s - napis; %d - wartosc liczbowa
print(message2 % ('file_1.txt', 100))

message3 = 'File %20s has size %10d KB' # ile znakow zarezerwowanych dla wartosci
print(message3 % ('file_1.txt', 100))

message4 = 'Processing file {0:s}'
print(message4.format('file1.txt'))

message5 = 'File {0:s} has size {1:d} KB'
print(message5.format('file1.txt',100))

message6 = 'File {1:s} has size {0:d} KB'
print(message6.format(100, 'file1.txt'))

message7 = 'File {0:20s} has size {1:10d} KB'
print(message7.format('file1.txt',100))

# zadania

helloMessage = "Hello %s!"
 
print(helloMessage % ("Kate"))
print(helloMessage % ("Chris"))
 
helloMessage = "Hello {0:s}!"
 
print(helloMessage.format("Kate"))
print(helloMessage.format("Chris"))
 
helloMessage = "%s has %d %s"
 
print(helloMessage % ("Kate",1,"animal"))
print(helloMessage % ("Chris",100000,"$"))
 
helloMessage = "{0:s} has {1:d} {2:s}"
 
print(helloMessage.format("Kate",1,"animal"))
print(helloMessage.format("Chris",100000,"$"))
 
line = "{0:20s} costs {1:6d} €"
 
print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAII',6))
 
line = '{0:s} {1:d}'
 
print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))