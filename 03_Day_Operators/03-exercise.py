# # Day 03: 30 days of python


# 1
age = int(21)

# 2
my_height = float(168)

# 3
num1 = complex(1+2j)

# 4
base, height = float(input("Enter the base: ")), float(input("Enter height: "))
area = 0.5 * base * height
print("Area of triangle is: ", area)



# 5
side1, side2, side3 = float(input("Enter side1: ")), float(input("Enter side2: ")), float(input("Enter side2: "))
print("Perimeter of the triangle is: ", side1 + side2 + side3)



# 6
length, breadth = float(input("Enter length: ")), float(input("Enter width: "))
print("Area of rectangle is: ", length * breadth)
print("Perimeter of reactangle is: ", 2 * (length+breadth))



# 7
PI = 3.14
radius = float(input("Enter radius: "))
print("Area of circle is: ", PI * radius ** 2)
print("Perimeter of circle is: ", 2 * PI * radius)



# 8
print('write the equation in slope intercept form')
x_coefficient = int(input("enter coffecient of x"))
y_coefficient = int(input("enter coefficient of y"))
constant = int(input("enter constant "))
print("slope is: ", x_coefficient)
print("x intercept is: ",constant * -1 /x_coefficient)


# 9
print("Given two points A(2,2) and B(6,10)")
x1,y1,x2,y2 = 2,2,6,10
m = (y2-y1 )/(x2- x1)
print("slope m = ",m)



#10
if m> x_coefficient:
    print(m , " is greater than ", x_coefficient, " from the previous question")
else:
    print(x_coefficient, " is greater than ",m, " from the previous question")



# 11
print("Given equation: y = x^2 + 6x + 9")
x = int(input("Enter a value for x"))
y = x**2 + 6*x + 9
print("value of y is: ", y)
print("when y = 0,")
x1 = (-6 + (((6 ** 2) - (4 * 9)) ** 0.5)) / 2
print(" x will be: ",x1)



# 12
var1, var2 = "python" , "dragon"
if len(var1)>len(var2):
    print(var1," is lengthiest with ",len(var1)," letters")
elif len(var2)> len(var1):
    print(var2, " is lengthiest with ", len(var2)," letters")
else:
    print("both are same length")



# 13
if "on" in var1 and var2:
    print(" found in both")
else:
    print("not found in both")



# 14
sentence = "i hope this course is not full of jargon"
if "on" in sentence:
    print("on found in sentence")
else:
    print("on not found in sentence")




# 15
if "on" not in var1 and var2:
    print("on not found in both")
elif "on" in var1 and "on" not in var2:
    print("found in ",var1)
elif "on" not in var1 and "on" in var2:
    print("found in ", var2)
else:
    print("found in both")



# 16
print(len(var1))

print(float(len(var1)))
print(str(len(var1)))



# 17
number = int(input("enter a number"))
if number % 2 ==0:
    print("even number")
else:
    print("not an even number")



# 18
value7 = 7 // 3  # value7 is 2
if value7 == int(2.7):
    print("yes ",value7," is same as int converted 2.7")



# 19
if type('10') == type(10):
    print("yes the types are equal")
else:
    print("the types are not equal")



# 20
if int(9.8) == 10:
    print("yes same")
else:
    print("not same")



# 21
hours = float(input("enter hours: "))
rate = float(input("enter rate per hour: "))
print("your weekly earning is: ",rate * hours)



# 22
years = int(input("enter number of years you have lived"))
print("you have lived for ",years * 31536000," seconds")



# 23
for i in range(1,6):
    for j in range(1,5):
        if j == 2:
            print(j-1,end=" ")
        if j>=3:
            print(i**(j-1),end=" ")
        else:
            print(i, end=" ")
    print()





##           OUTPUT     ##

# Enter the base: 10
# Enter height: 20
# Area of triangle is:  100.0
# Enter side1: 3
# Enter side2: 6
# Enter side2: 3
# Perimeter of the triangle is:  12.0
# Enter length: 5
# Enter width: 6
# Area of rectangle is:  30.0
# Perimeter of reactangle is:  22.0
# Enter radius: 5
# Area of circle is:  78.5
# Perimeter of circle is:  31.400000000000002
# write the equation in slope intercept form
# enter coffecient of x 6
# enter coefficient of y 4
# enter constant 2
# slope is:  6
# x intercept is:  -0.3333333333333333
# Given two points A(2,2) and B(6,10)
# slope m =  2.0
# 6  is greater than  2.0  from the previous question
# Given equation: y = x^2 + 6x + 9
# Enter a value for x 6
# value of y is:  81
# when y = 0,
#  x will be:  -3.0
# both are same length
#  found in both
# on found in sentence
# found in both
# 6
# 6.0
# 6
# enter a number 7
# not an even number
# yes  2  is same as int converted 2.7
# the types are not equal
# not same
# enter hours: 45
# enter rate per hour: 3
# your weekly earning is:  135.0
# enter number of years you have lived 21
# you have lived for  662256000  seconds
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
