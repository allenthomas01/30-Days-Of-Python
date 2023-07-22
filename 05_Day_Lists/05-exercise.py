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

