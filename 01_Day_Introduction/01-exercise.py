spacer="\n*******************\n" # just for some formatting

# level 2

print(spacer,"LEVEL 2",spacer)
print(spacer,"python version",spacer)
import sys
print(sys.version)

print(spacer,"operations on numbers",spacer)
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4) 
print(3//4) 


print(spacer,"strings",spacer)
print('Allen')
print("India")
print('I am enjoying 30 days of python')
print(spacer,"check data types",spacer)
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Allen','Python','India']))
print(type('Allen'))

# level 3

print(spacer,"LEVEL 3",spacer)
print(spacer,"examples for data types",spacer)
intNum = 4
floatNum = 3.2
complexNum = 3+1j
stringVar = 'allen'
stringVar2 = "howdy"
multiline_string= """ this
is a multiline
string
"""
booleanVar = True
boolearnVar2 = False
listVar = ['member1','member2',7,1] #different data types
tupleVar = (8,1,'allen') #unmutable,different data types
setVar = {3,'bob',1} #orders elements, so after becomes {1,'bob',3}
dictionaryVar = {
    'myname':'allen',
    'myage':21,
    'my passion':'writing scripts'
}
print(intNum,floatNum,complexNum,stringVar,stringVar2,multiline_string,booleanVar,boolearnVar2,listVar,tupleVar,setVar,dictionaryVar,sep="\n")


"""  OUTPUT

 *******************
 LEVEL 2 
*******************


*******************
 python version 
*******************

3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]

*******************
 operations on numbers 
*******************

7
-1
12
3
0.75
81
0

*******************
 strings 
*******************

Allen
India
I am enjoying 30 days of python

*******************
 check data types 
*******************

<class 'int'>
<class 'float'>
<class 'float'>
<class 'complex'>
<class 'list'>
<class 'str'>

*******************
 LEVEL 3
*******************


*******************
 examples for data types
*******************

4
3.2
(3+1j)
allen
howdy
 this
is a multiline
string

True
False
['member1', 'member2', 7, 1]
(8, 1, 'allen')
{'bob', 1, 3}
{'myname': 'allen', 'myage': 21, 'my passion': 'writing scripts'} """