#global a
a = 1
b = 2

def funkcja(z):
    global d    # global pozwala odniesc sie do zmiennej w calym kodzie po zadeklarowaniu
    d = 3
    print(a * b * d * z)
    z += 1
    return

c = int(input("Podaj zmienna liczbowa: "))
funkcja(c)
print("c =", c)
print(d)