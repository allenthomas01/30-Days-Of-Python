# 30 days of python

# Day 05

# 1
zero = []

# 2
five = ['first',2,'third','fourth',5,6,'seven']

# 3
length = len(five)
print(length)

# 4
length = len(five)
first = five[0]
middle = int((length-1)/2)
middle_element = five[middle]
last = five[length-1]
print(first,middle_element,last)

# 5
mixed_data_types = ['allen',21,168,'no','kerala India']


# 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]

# 7
print(it_companies)

# 8
length = len(it_companies)
print('Number of companies is {}'.format(length))

# 9
first = it_companies[0]
middle = it_companies[int((length + 1 ) /2)]
last = it_companies[int(length-1)]
print('First: {} , middle: {} ,last: {}' .format(first,middle ,last))

# 10
it_companies[0] = 'Meta'
print(it_companies)

# 11
it_companies.append('TCS')
print(it_companies)

# 12
length = len(it_companies)
it_companies.insert(int((length + 1) /2),'Goldman Sachs')
print(it_companies)

# 13
first = it_companies[0]
it_companies[0] =first.upper()
print(it_companies)

# 14
it_companies.extend('#')
print(it_companies)
it_companies.pop()

# 15
bool = 'Google' in it_companies
print(bool)

# 16
it_companies.sort()
print(it_companies)

# 17
it_companies.sort(reverse=True)
print(it_companies)

# 18
slice1 = it_companies[0:3]
print(slice1)

# 19
slice2 = it_companies[-3:]
print(slice2)

# 20
middle = int((len(it_companies)-1)/2)
middle_slice = it_companies[middle]
print(middle_slice)

# 21
del it_companies[0]
print(it_companies)

# 22
middle = int((len(it_companies)-1 )/2)
del it_companies[middle:middle+2]
print(it_companies)

# 23
it_companies.pop()
print(it_companies)

# 24
it_companies.clear()
print(it_companies)

# 25
del it_companies

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# 27
fullstack = front_end.copy()
fullstack.append('python')
fullstack.append('SQL')
print(fullstack)

# Exercise : level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print('Min age: {} , Max age: {}'.format(ages[0],ages[len(ages)-1]))
ages.append(19)
ages.append(26)
ages.sort()
middle = int((len(ages)-1)/2)
print('Median age: {}'.format(ages[middle]))

sum = 0
for i,n in enumerate(ages):
    sum = sum + n
print('Average age is {}'.format(sum/len(ages)))

maxValue = max(ages)
minValue = min(ages)
print('Range of ages is {}'.format(maxValue-minValue))

average = int(sum / len(ages))
print('(min - average) = {} \t (max-average)={}'.format(abs(minValue-average),maxValue-average))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# 1
middle = int((len(countries)-1)/2)
print(countries[middle])

# 2
length = len(countries)
print(length)
middle = int(((length-1)/2))
if length%2==0:
    print(countries[0:middle])
else:
    print(countries[0:middle+1] , countries[middle+1:])

# 3
first , second, third, *rest = countries
print(first,second,third,rest)

##########################3

# OUTPUT

# 7
# first fourth seven
# ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Number of companies is 7
# First: Facebook , middle: IBM ,last: Amazon
# ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'TCS']
# ['Meta', 'Google', 'Microsoft', 'Apple', 'Goldman Sachs', 'IBM', 'Oracle', 'Amazon', 'TCS']
# ['META', 'Google', 'Microsoft', 'Apple', 'Goldman Sachs', 'IBM', 'Oracle', 'Amazon', 'TCS']
# ['META', 'Google', 'Microsoft', 'Apple', 'Goldman Sachs', 'IBM', 'Oracle', 'Amazon', 'TCS', '#']
# True
# ['Amazon', 'Apple', 'Goldman Sachs', 'Google', 'IBM', 'META', 'Microsoft', 'Oracle', 'TCS']
# ['TCS', 'Oracle', 'Microsoft', 'META', 'IBM', 'Google', 'Goldman Sachs', 'Apple', 'Amazon']
# ['TCS', 'Oracle', 'Microsoft']
# ['Goldman Sachs', 'Apple', 'Amazon']
# IBM
# ['Oracle', 'Microsoft', 'META', 'IBM', 'Google', 'Goldman Sachs', 'Apple', 'Amazon']
# ['Oracle', 'Microsoft', 'META', 'Goldman Sachs', 'Apple', 'Amazon']
# ['Oracle', 'Microsoft', 'META', 'Goldman Sachs', 'Apple']
# []
# ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
# ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB', 'python', 'SQL']
# Min age: 19 , Max age: 26
# Median age: 24
# Average age is 22.75
# Range of ages is 7
# (min - average) = 3 	 (max-average)=4
# Finland
# 7
# ['China', 'Russia', 'USA', 'Finland'] ['Sweden', 'Norway', 'Denmark']
# China Russia USA ['Finland', 'Sweden', 'Norway', 'Denmark']





