# import cv2
import math

# # This is a comment
# print("Hello World")
# print(math.gcd(3,6))
# '''
# This is a multi line comment
# by using this you can write anything and with any lenghth
# '''
# print(5+8)
# age= 20
# if(age<18):
#     print("hello")
# else:
#     print("no")

a = 34 
b = "yash"
c = 45.32
d = 3

# print(a + d)
# print(a - d)
# print(a * d)
# print(a / d)

# Wrong syntax
# Yash Project = 44
# rules for creating variables

# 1. Variables shoullld start with a letter or an underscore
# 2. Variable cannot start with a number
# 3. It can only contain alphanumaric characters 
# 4. Variable names are case sensitive . Yash and yash are two different variables 

# typeA = type(a)
# typeB = type(b)
# print(typeB)
e = "31"
# e = float(e)
# e = str(455)  
e = int("34")
# if you write a number as a string and want to convert that into integer/float/string, this is type casting
# e =  3.14
# print(type(e))
# print(e+2)

# name = '''Yash
#  is working''' 
# #this is how you can layer the string
# print(name[0])
#if you write 0 it will come up as a first character

name = "Yash, Raj, james"
# print(name[1:3])
# print(name)
# print(name.strip())  this will help to remove extra space from string if any. exp: "  yash  "
# print(len(name)) this is to know the length of the string. Exp "yash" this has 4 letter show the output will be that
var = name.lower() #this to write all the letters in lower case
var = name.upper() #this to write all the letters in upper case
var = name.replace("s", "a") #this to write all the letters in replace case
var = name.replace(", ", '\n') #if you wanna replace ',' to blank or '\n'(this is a new line character)
# print(var)

stri = "This is a "
name1 = "Yash"
name2 = "Raj"
stri2 = "This is not a"
# print(stri + name) to merge 2 strings 
# temp = "This is a {} and he is a good boy named {}".format(name1, name2)
temp = f"this is a {name2} and he is a good boy named {name1}" # By using f string you can directly write string name in {} and print the format
# print(temp)

''' 
Python collections:
1. List
2. Tuple
3. Set
4. Dictionary

''' 

list = [61,2,3,4,6,41] #list is a order or collection which can be changed
# var = type(list)
# list[2] = 45
# var = list[2] #with this we can do slicing of the variable
# list.append(100) #append add written element into list
# list.insert(1,100) #to insert and element at the place provided
# list.remove(61) this is to remove any element from list
# list.pop() #for removing end element from the list 
# del list[3] #to deelete and element at the given postion
# list.clear() #this is to clear the list totally
var = list
# var = len(list)


#Tuple "you can not chamge the value of the tuple"
a = ("Yash", "Shubh", "Raj")
# var = a
# a =  lst(a)
var = type(a)

# cannot do this
# a[0] = "Vikrant"
# print(var)

# Set (set is a collection of well defined object)
s1 = {23,2,2,2,2,2,3,2,1,2,4,12,7,12,3} #by using set it will not gonna repeat element 
# s1.add(4444) #this is to add any element is set which is not there 
# s1.update([12,1,28,334,4,343,43453,3232])
# print(len(s1)) #will show you the number of elements in that 
# s1.remove(1) #to rremove number which already exist in the set
# s1.discard(1555) #by using this if the element is there it will get removed and if not it will pass through with no errors
# like list you can use some function: .pop, .clear, del, 
# and intersection, union 
# print(s1)

# Dictionary (key value peirse )

yashdict = {
    "Name": "Yash",
    "Class": "4th",
    "Marks": 34.3,
    "Hours In School": 6
}
yashdict["Marks"] = 34
# print(yashdict["Marks"]) #you can change the element and print it
yashdict.pop("Marks") #after using pop/del/clear to remove any element from the dictionary
# print(yashdict)

#conditional Statement:

# age = 34
# age = input("Enter Your Age\n") #this is to take input from the system
# age = int(age)

# print(type(age))
# if(age>18):
#     print("You can drive a car")
# elif(age==18):
#     print("You are an awesome teen")

# else: 
#     print("You cannot drive")

# Loops: 
# scenario: you have to print a number between 1 to 1000
# for i in range (0,1000):
    # print(i+1) #the count strat from 0 so in that case you have to write +1 so it can give you numbers till 1000

# li = [1, 432, "This"]
# for item in li:
#     print(item) # It will print all the item which is in li variable

# i = 0 
# while (i<100):
#     print(i+1)
#     if i == 78:
#         break #this means after 78 it will stop the loop their 
#     i = i + 1

# FUnctions: (block of code that you can run by calling its name)
# def greet():
#     print ("Good morning sir")
#     print ("Good morning madam")

# greet()

# def sum(a,b): #you can do any comutation by usning this function
#     c = a +b
#     return c

# d = sum(34 , 45)
# print(d)


# class Employee:
#     def __init__(self, gname, gsalary):
#         self.name = gname
#         self.salary = gsalary

# yash = Employee("yash", 44)
# print(yash.name)
# print(yash.salary)

# Fruits = ["apple", "kiwi", "kiwi", "apple", "mango", "watermelon", "dragonfruit"]
# count = {}
# for i in Fruits:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1

# for i,k in count.items():
#     print(i," ",k)

# print(math.floor(1.4))

# def sum(a,b):
#     Yash = a+b

#     return Yash
# a,b=4,5
# yash = sum(a,b)
# print(yash)

# list = [1,3,2,4,5,99,14,2,2,5,4,3]
# # print(list.count(1))
# # list.append(99)
# list2 = [30]
# # list.extend(list2)
# # list.insert(3, 30)
# list.sort()
# print(list)


# Car = lambda c,d:c+d #by usning this function you can write in one line
# print(Car(4,7))

# try:
#     print(1/0)
# except Exception as e:
#     print(e) #it will come here in except log if any error will come otherwise it will all pass 
# finally:
#     print("completed")


# class Top:
#     d=4
#     e=5
#     f=6
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def sum(self):
#         print("f")
#     def sum(g,h):
#         print(g+h)    

# Son = Top(1,2,3)

# Son.sum()
# Son.sum(7,8)

class Top:
    d = 4
    e = 5
    f = 6
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def sum(self):
        print("f")
        
    def sum_with_params(self, g, h):
        print(self.a + self.b + self.c + g + h)

class SubTop(Top):  # Subclass inheriting from Top
    def sum(self):
        print("Overridden sum method in SubTop")
        
    def sum_with_params(self, g, h):
        print("Overridden sum_with_params method in SubTop:", self.a + self.b + self.c + g + h)

# Example usage:
obj1 = Top(1, 2, 3)
obj2 = SubTop(1, 2, 3)

obj1.sum()  # This will call the sum method in Top class and print "f"
obj1.sum_with_params(7, 8)  # This will call the sum_with_params method in Top class

obj2.sum()  # This will call the overridden sum method in SubTop class and print "Overridden sum method in SubTop"
obj2.sum_with_params(7, 8)  # This will call the overridden sum_with_params method in SubTop class
    



