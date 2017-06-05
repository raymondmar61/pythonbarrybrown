#sets can hold any number of values, elements are unordered, no duplicates, and support set operations: union, intersection, difference, etc.
#sets are typed inside curly braces
set1 = {10, 56, 1, 4}
print(set1)
set2 = {10, 56, 10, 4, 56, 7}
print(set2)
setnames = {"Bob", "Sue","Jane"}
print(setnames)
a = {1, 2, 3, 4}
b = {2, 4, 7, 5, 6}
c = {9, 1, 4, 3}
d = {2, 4}
print(a, b, c, d) #print all the sets.  Wow, it tctually printed each set separated by a space
print(a | b) #union set a and set b no duplicates
print(a & b) #intersection set a and set b
print(a - c) #difference takes elements from set a and subtracts from set c.  Any elements remain in set a is printed
print(a ^ c) #"exclusive or" which finds set a or set c not both a and c
print(d < b) #subset.  Are all elements in set d present in set b?
print(d < a) #subset.  Are all elements in set d present in set a?
print(d < c) #subset.  Are all elements in set d present in set c?
print(9 in {3, 6, 9}) #is 9 in set {3, 6, 9}
print(7 in b) #is 7 in set b
print(100 in a) #is 100 in set a

#setbuilder
#construct the first ten numbers to the powers of 2.  2, 4, 8, 16, 32, . . . 1024
#{2**x for x in range(1, 11)}
power = set()
# for x in range(1, 11):
# 	print(2**x)
# 	power.add(2**x)
[power.add(2**x) for x in range(1, 11)] #curly brackets also worked same as brackets
print(power)

boys = {"Bob","Henry","Jason"}
girls = {"Heather","Jen","Michelle","Maria"}
#print all the pairings for the boys and girls
# for b in boys:
# 	for g in girls:
# 		print(b, g)
{print(b, g) for b in boys for g in girls} #brackets also worked

teams = {"Tigers","Badgers","Generals"}
#[print(a, b) for a in teams for b in teams] #problem, tigers vs tigers, badgers vs badgers
[print(a, b) for a in teams for b in teams if a != b]

#take two sets of numbers 1-10, add them, return pairs of numbers divisible by 5
# divisible5 = set()
# for x in range(1, 11):
# 	for y in range(1, 11):
# 		if (x + y) % 5 == 0:
# 			divisible5.add((x, y))
# print(divisible5)
divisible5 = set()
{divisible5.add((x, y)) for x in range(1, 11) for y in range(1, 11) if (x + y) % 5 == 0}
print(divisible5)


#side note:  Practice Python Exercise 5 listoverlap
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# a = set(a)
# b = set(b)
# print(a & b) #returns {1, 2, 3, 5, 8, 13}