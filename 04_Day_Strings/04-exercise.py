# Day 04: 30 days of python

# 1
str1 = ' thirty'
str2= ' days'
str3 = ' of'
str4 = ' python'

sent1 = str1 +str2+str3+str4
print(sent1.title())

# 2
# same as 1

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

#6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[0:6])

# 10
print(company.index('Coding'))
print(company.find('Coding'))

# 11
company = company.replace('Coding', 'Python')
print(company)

# 12
company = company.replace('All','Everyone')
print(company)

# 13
print(company.split())

# 14
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company.split(','))

# 15
company = "Coding For All"
print(company[0])

# 16
print(len(company)-1)

# 17
print(company[10])

# 18
company = 'Python For Everyone'
print(company[0::2])

# 19
company = 'Coding For All'
print(company[0::3])

 # 20
print(company.index('C'))

# 21
print(company.index('F'))

 # 22
company = 'Coding For All People'
print(company.rfind('I'))

# 23
company = "You cannot end a sentence with because because because is a conjunction"
print(company.find('because'))

# 24
print(company.rindex('because'))

#25
print(company[31:54])

# 26
print(company.rfind('because'))

# 27
print(company[31:54])

# 28
company = "Coding For All"
print(company.startswith('Coding'))

# 29
print(company.endswith('coding'))

# 30
company = '   Coding For All      ' 
print(company.split())

# 31
# thirty_days_of_python


# 32
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
output = '# '.join(list)
print(output)

# 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34
print("Name\tAge\tCountry\tCity\nAllen\t21\tIndia\tKottayam")

# 35
radius =10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area} meters square.')

print('The area of a circle with radius {} is {} meters square'.format(radius,int(area)))

# 36
eight = 8
six= 6
print('{} + {} = {}'.format(eight,six,eight+six))
print('{} - {}= {}'.format(eight,six,eight-six))
print('{} * {} = {}'.format(eight,six,eight*six))
print('{} / {} = {:.2f}'.format(eight,six,eight/six))
print('{} % {} = {}'.format(eight,six,eight%six))
print('{} // {} ={}'.format(eight,six,eight//six))
print('{} ** {} = {}'.format(eight,six,eight**six))