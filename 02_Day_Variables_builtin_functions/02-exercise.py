#Day 2 : 30 days of python programming

#level 1
first_name = 'allen'
last_name = 'thomas'
full_name = 'allen thomas'
country = 'India'
city = 'Kottayam'
age = 21
year = 2001
is_married = False
is_true=True 
is_light=False

hobbie1,hobbie2 = 'badminton','reading'
# level 2
#2.1
print("type of firstname:",type(first_name))
print("type of lastname:",type(last_name))
print("type of fullname:",type(full_name))

#2.2
print("length of firstname:",len(first_name))

#2.3
print("length of firstname:",len(first_name)," and ","length of lastname:",len(last_name))

#2.4
num_one,num_two  = 4,5
total = num_one + num_two
diff= num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

#2.5
r,PI=30,3.14
#2.5.1
area_of_circle =  PI * r**2
print("area of circle with radius ",r," is: ",area_of_circle)
#2.5.2
circum_of_circle = 2 * PI * r
print("circumference of circle with radius ",r ,"is: ",circum_of_circle)

#2.5.3
print("Enter new radius of circle:")
r = int(input())
print("area is: ",PI*r**2)

#2.6
print("enter first name,last name,country and age")
first_name,last_name,country,age = input(),input(),input(),int(input())
print("you entered:::","\tfirst_name: ",first_name,"\tlast_name: ",last_name,"\tcountry: ",country,"\tage: ",age)





"""   OUTPUT

type of firstname: <class 'str'>
type of lastname: <class 'str'>
type of fullname: <class 'str'>
length of firstname: 5
length of firstname: 5  and  length of lastname: 6
area of circle with radius  30  is:  2826.0       
circumference of circle with radius  30 is:  188.4
Enter new radius of circle:
5
area is:  78.5
enter first name,last name,country and age
allen
thomas
india
21
you entered:::  first_name:  allen      last_name:  thomas      country:  india         age:  21 
"""