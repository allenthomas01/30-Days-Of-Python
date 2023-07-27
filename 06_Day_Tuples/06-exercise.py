# 30 Days of python

# Day 06


# level 1

# 1
empty_tuple = ()
print(empty_tuple)  #()

# 2
brothers = ('one','two','three')
sisters = ('four','five','six')

# 3
siblings = brothers + sisters
print(siblings)  #('one', 'two', 'three', 'four', 'five', 'six')

# 4
print(len(siblings)) # 6

# 5
family_members = list(siblings)
family_members.append('seven')
family_members.append('eight')
print(family_members) #['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']

# level 2

# 1
mother,father,* siblings = family_members[::-1]
print(mother,father,siblings) # eight seven ['six', 'five', 'four', 'three', 'two', 'one']

# 2
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products=('meat','egg','milk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp) # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot', 'meat', 'egg', 'milk')

# 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)# ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot', 'meat', 'egg', 'milk']

# 4
middle = int((len(food_stuff_tp)-1)/2)
print(food_stuff_tp[middle])  # Potato


# 5
first_three = food_stuff_lt[0:3]
last_three =  food_stuff_lt[-3:]
print(first_three, last_three)  # ['banana', 'orange', 'mango'] ['meat', 'egg', 'milk']

# 6
del food_stuff_tp

# 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)  # False
print('Iceland' in nordic_countries)  # True

