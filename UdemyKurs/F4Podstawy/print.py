'''
(*values: object, sep: str | None = " ", end: str | None = "\n", file: SupportsWrite[str] | None = None, flush: Literal[False] = False) -> None
Prints the values to a stream, or to sys.stdout by default.

sep
  string inserted between values, default a space.
end
  string appended after the last value, default a newline.
file
  a file-like object (stream); defaults to the current sys.stdout.
flush
  whether to forcibly flush the stream.
'''

print("FR")
print("FR","DE","UK")
France = "FR"
print(France,"DE","UK")
pi = 3.14
r = 10
print(pi, r, pi*r*r)
print(pi, r, pi*r**2) # potegowanie, po ** wykladnik potegi
print(1,2,3)
print(1,2,3, sep='-')
print(1,2,3, sep='\n') # w kolejnych liniach
print(1,2,3, sep='\t') # oddzielone tabulatorem
print("this is a bell: \a") # dziala w konsoli Python

print("\u03A3") # wyswietlanie znakow, tu znak Sigma
print("this is backslash: \\")

print('TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV')
print('TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=';')
print('I like computers ','TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=' but better is ')
ProgramName = 'BBC'
Item = 'News'
Time = '18:00'
print('I like watching',Item,'at',Time,'on',ProgramName,'.')
print('I like watching ',Item,' at ',Time,' on ',ProgramName,'.', sep='')