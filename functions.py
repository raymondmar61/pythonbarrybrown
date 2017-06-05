def cube(x):
	"""Give a number, number is cubed"""
	return x**3
print(cube(3)) #prints 27

def squares(start,end):
	"""Give a range of numbers, returns all square numbers from start to end"""
	squarenumbers = []
	for eachnumber in range(start,end+1):
		squarenumbers.append(eachnumber**2)
	print(squarenumbers)
squares(1,5) #returns [1, 4, 9, 16, 25]

def odds_under(n):
	"""Return a list of positive odd numbers less than n"""
	oddnumberlist = []
	for eachnumber in range(0, n):
		if eachnumber % 2 == 1:
			oddnumberlist.append(eachnumber)
	print(oddnumberlist)
odds_under(26) #returns [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

def evenoroddlist(nums):
	"""Submit a list of numbers to check even or odd"""
	evenoddlist = []
	i = 0
	while i < len(nums):
		if nums[i] % 2 == 0:
			evenoddlist.append("even")
		elif nums[i] % 2 == 1:
			evenoddlist.append("odd")
		else:
			evenoddlist.append("")
		i = i + 1
	return evenoddlist
print(evenoroddlist([-9,-250,1,2,3,4,5,100, 102, 104, 1001, 9999])) #prints ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'even', 'even', 'odd', 'odd']