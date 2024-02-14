import sys

# int - liczby calkowite
# float - liczby niecalkowite, nie jest dokladnym typem, bo zaokragla

five = 5
three = 3
print(type(five * three))

print(type(five / three))

print(sys.maxsize)

veryBigValue = 999999999999999999999999999999999999999999999999999999
print(type(veryBigValue))

print((veryBigValue+1)/2) # zapis wyniku 5e+53
print(type((veryBigValue+1)/2))

print(five // three) # dzielenie calkowite dwa backsplashe

print(five % three) # dzielenie modulo, ile zostaje reszty

# zadania

name = 'Jan'
age = 26
daysInYear = 365
message = '%s is %d years old, so is about %d days old'
print(message % (name,age,age*daysInYear))
name = 'Chris'
age = 17
print(message % (name,age,age*daysInYear))
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format(name,age,age*daysInYear))
print('1234567890 divided by 12345 is ',1234567890 // 12345,'and the rest is',1234567890 % 12345)