#tuples group togehter related values in paranthesis; for example, (x, y, z) coordinates, (name, age) pairs ("Bob",19) ("Jane", 23).  Can hold any number of values.  Can't add or remove elements.  Elements are ordered.  Tuples are immutable or can't change elements.
a = (4, 5)
b = ("Bob",19)
print(b) #returns ('Bob', 19)
print(a[0])
print(b[0])
print(b[1])
range(4, 10) #The (4, 10) is a tuple
print(divmod(37, 5)) #returns tuple (7, 2) quotient 7 and remainder 2
(q, r) = divmod(37, 5)
print(q) #returns 7
print(r) #returns 2