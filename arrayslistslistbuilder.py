#Lists are also called Array or Vector
numberlist = [1, 2, 3, 4]
numberlist = [1, 4, 5, 2, 7]
numberlist = [5, 2, 4, 5, 7, 2]
a = [1, 2, 3, 4]
names = ["Bob","Sue","John"]
print(a)
print(names)
print(a[0])
print(names[2])
a.append(8)
print(a[4]) #returns 8
a[2] = 10
print(a) #returns [1, 2, 10, 4, 8]
print(range(4,11)) #returns range(4,10)
print(list(range(4,11))) #returns [4, 5, 6, 7, 8, 9, 10]

listx = []
[listx.append(x * 2) for x in range(1, 11)]
print(listx) #returns [2, 4, 6, 8, 10, 12, 14, 16, 18, 20

listy = []
[listy.append(x) for x in range(2, 21) if x % 2 == 0]
print(listy) #returns [2, 4, 6, 8, 10, 12, 14, 16, 18, 20

okay = [1, 2, 10, 4, 8]
count = 0
while count < len(okay):
	okay[count] += 1
	count += 1
print(okay) #returns [2, 3, 11, 5, 9]
#[print(list(z)) for z in okay if z >=8] #error message
[print(z) for z in okay if z >=8] #returns 11 \n 9
okaynew = []
for z in okay:
	if z >= 8:
		okaynew.append(z)
print(okaynew) #returns [11, 9]

print("Hello World!")
hi = "Hello World!"
print(hi[0]) #returns H
print(hi[10]) #returns d
print(hi[11]) #returns !
print(list(hi)) #returns ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
print(ord("H")) #returns ASCII value which is 72
for eachhi in hi:
	print(ord(eachhi), end=" ") #returns 72 101 108 108 111 32 87 111 114 108 100 33