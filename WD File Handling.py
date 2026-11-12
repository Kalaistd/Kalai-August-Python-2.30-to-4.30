#file Handling

#create a new file
# a=open("C:/Users/ELCOT/Desktop/kalai.txt","x")
#

# Write a file
# a=open("C:/Users/ELCOT/Desktop/kalai.txt","w")
# a.write("I love India")
# a.close()
# print("success")


# Append a file
# a=open("C:/Users/ELCOT/Desktop/kalai.txt","a")
# a.write("I love India!!!!!!!")
# a.close()
# print("success")


# # Read a file
# a=open("C:/Users/ELCOT/Desktop/kalai.txt","r")
# print(a.read())

# # To delete a file
# import os
# os.remove("C:/Users/ELCOT/Desktop/kalai.txt")

##Exception Handling

# try:
#     x=10
#     print(y)
# except Exception as e :
#     print(e)
# finally:
#     print("operation  done")


# Example for raise
# try:
#     a=int(input("enter a num"))
#     b=int(input('enter a num'))
#     if b==0:
#         raise ZeroDivisionError('denominator  should not be 0')
#     c=a+b
#     d=a-b
#     e=a/b
#     print(c,d,e)
# except Exception as e:
#     print(e)
# finally:
#     print("operation done")


# 1.Example for assert
# x="hello"
# assert x=="Hai"
# print(x)



# # 2.Example for assert
# x="hello"
# assert x=="hello"
# print(x)

###=====================================================================

# Example for class and object
# class Janani: #class classname
#     def fun(): #function
#         print("hiii")
# x=Janani()# Object for class
# x.fun() #using object to get the function


# class Car:
#     def start(self):
#         print(f"{self.brand} car is starting")
#
# car1 = Car()
#
# car1.brand = "Toyota"
# car1.color = "White"
# print(car1.brand)
# print(car1.color)
# car1.start()


# class Student:
#     # Method
#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Course: {self.course}")
#
#
# # Creating an object
# student1 = Student()
#
# # Assigning attributes manually
# student1.name = "Arun"
# student1.age = 21
# student1.course = "Python"
#
# # Creating another object
# student2 = Student()
#
# student2.name = "Priya"
# student2.age = 20
# student2.course = "Data Science"
#
# # Calling methods
# student1.display_details()
#
# print()
#
# student2.display_details()



# class demo:
#     def __init__(self):
#         self.name="python"
#         print("hiii")
# class demo1(demo):
#     def fun2(self):
#         print(self.name)
# x=demo1()
# x.fun2()

# # Example for class and object
# class Janani: #class classname
#     def fun(self): #function
#         print("hiii")
# x=Janani()# Object for class
# x.fun() #using object to get the function


#
# class Car: #class classname
#     def start(self): #function
#         print(f"{self.brand} car is starting")
# c = Car() #object for class
# c.brand = "Toyota"
# c.color = "White"
# print(c.brand)
# print(c.color)
# c.start() #using object to get the fn


# # Example for constructor
# class demo:
#     def __init__(self):
#         self.name="python"
#         print("hiii")
# class demo1(demo):
#     def fun2(self):
#         print(self.name)
# x=demo1()
# x.fun2()



# x=input("Enter the String:")
# w=" "
# for i in x:
#     w=i+w
# if (x==w):
#     print("Yes")
# else:
#     print("No")



# Example:

# class Student:
#     # Method
#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Course: {self.course}")
#
#
# # Creating an object
# student1 = Student()
#
# # Assigning attributes manually
# student1.name = "Arun"
# student1.age = 21
# student1.course = "Python"
#
# # Creating another object
# student2 = Student()
#
# student2.name = "Priya"
# student2.age = 20
# student2.course = "Data Science"
#
# # Calling methods
# student1.display_details()
#
# print()
#
# student2.display_details()



# class Animal:
#     def eat(self):
#         print("Eating")
#
# class Dog(Animal):
#     pass
#
# d = Dog()
# d.eat()

#
# # 5. Hybrid Inheritance
# class Animal:
#     def eat(self):
#         print("Eating")
#
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
#
# class Cat(Animal):
#     def meow(self):
#         print("Meowing")
#
# class Puppy(Dog, Cat):
#     pass
#
# p = Puppy()
# p.eat()
# p.bark()
# p.meow()







#
# ==================================================================================
#


#Classes & Objects

# # Example for class and object
# class Janani: #class classname
#     def fun(self): #function
#         print("hiii")
# x=Janani()# Object for class
# x.fun() #using object to get the function


# class Car: #class classname
#     def start(self): #function
#         print(f"{self.brand} car is starting")
# c = Car() #object for class
# c.brand = "Toyota"
# c.color = "White"
# print(c.brand)
# print(c.color)
# c.start() #using object to get the fn



#
# # Example:
#
# class Student:
#     # Method
#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Course: {self.course}")
#
# # Creating an object
# student1 = Student()
# # Assigning attributes manually
# student1.name = "Arun"
# student1.age = 21
# student1.course = "Python"
#
#
# # Creating another object
# student2 = Student()
# student2.name = "Priya"
# student2.age = 20
# student2.course = "Data Science"
#
# # Calling methods
# student1.display_details()
# print()
# student2.display_details()

# # Example for constructor
# class demo:
#     def __init__(jan):
#         jan.name="python"
#         print("hiii")
# class demo1(demo):
#     def fun2(jan):
#         print(jan.name)
# x=demo1()
# x.fun2()


##########################################################################################

#Inheritance

# # 1.Single Inheritance
# class Animal:
#     def eat(self):
#         print("Eating")
#
# class Dog(Animal):
#     pass

# d = Dog()
# d.eat()



# # 2.Multilevel Inheritance
# class Vehicle:
#     def start(self):
#         print("Vehicle started")
#
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")
#
# class SportsCar(Car):
#     def turbo(self):
#         print("Turbo mode activated")
#
# s = SportsCar()
# s.start()
# s.drive()
# s.turbo()





# # 3.Multiple Inheritance
# class Father:
#     def money(self):
#         print("Father's Money")
#
# class Mother:
#     def love(self):
#         print("Mother's Love")
#
# class Child(Father, Mother):
#     pass
#
# c = Child()
#
# c.money()
# c.love()



# # 4.Hierarchical Inheritance
# class User:
#     def login(self):
#         print("User logged in")
#
# class Customer(User):
#     def place_order(self):
#         print("Customer placed an order")
#
# class Seller(User):
#     def add_product(self):
#         print("Seller added a product")
#
# class DeliveryPartner(User):
#     def deliver_order(self):
#         print("Order delivered")
#
# c = Customer()
# s = Seller()
# d = DeliveryPartner()
#
# c.login()
# c.place_order()
# s.add_product()
# d.deliver_order()
#

#
#
# # 5. Hybrid Inheritance
# class Animal:
#     def eat(self):
#         print("Eating")
#
# class Dog(Animal):
#     def bark(self):
#         print("Barking")
#
# class Cat(Animal):
#     def meow(self):
#         print("Meowing")
#
# class Puppy(Dog, Cat):
#     pass
#
# p = Puppy()
# p.eat()
# p.bark()
# p.meow()



#Constructor

# class demo:
#     def __init__(self):
#         self.name="python"
#         print("hiii")
# class demo1(demo):
#     def fun2(self):
#         print(self.name)
# x=demo1()
# x.fun2()


# # Ex:
# class Database:
#     def __init__(self):
#         print("Database Connected")
#     def __del__(self):
#         print("Database Connection Closed")
# db = Database()
# del db


# class demo:
#     def __init__(self,name):
#         self.name=name
#         print("im constructor")
#         print("hiii")
#     def __del__(self):
#             print('object is detected')
# x=demo("Python")
# del x



#function overloading
#
# # Example
# class calculator:
#     def Addition(self,a=None,b=None,c=None,d=None):
#         if a!=None and b!=None and c!=None:
#             d=a+b+c
#             print("ADD of",a,b,c,"is",d)
#         elif a!=None and b!=None:
#             c=a+b
#             print("result of a,b is",c)
#         else:
#             print("value of a is:",a)
# obj=calculator()
# obj.Addition(100,200,300)
# obj.Addition(100)
# obj.Addition(10,20)



#function over riding

# class details:
#     def A(self):
#         print("Im first function")
#
# class display(details):
#     def A(self):
#         super().A()
#         print("Im second  function")
#         # super().A()
#
# obj=display()
# obj.A()



# Example for operator overloading
# a=input("enter 1st number")
# print(type(a))
# b=input("enter secKalaiond number")
# print(a+b)
#
#
# a=int(input("enter 1st number"))
# print(type(a))
# b=int(input("enter second number"))
# print(a+b)



#abstraction

# from abc import ABC, abstractmethod
# class demo(ABC):
#     @abstractmethod #decorator
#     def disp(self):
#         pass
# class demo1(demo):
#     def disp(self):
#         print("abstract method")
# obj=demo1()
# obj.disp()


# Example for abstraction
# from abc import ABC, abstractmethod
#
# class Payment(ABC):
#     @abstractmethod #decorator
#     def pay(self):
#         pass
#
# class UPI(Payment):
#     def pay(self):
#         print("Payment done through UPI")
#
# class CreditCard(Payment):
#     def pay(self):
#         print("Payment done through Credit Card")
#
# u = UPI()
# c = CreditCard()
#
# u.pay()
# c.pay()



#encapsulation
# Example of Encapsulation

# class demo():
#     __name="live"
#     def __display():
#         print("name is",demo.__name)
#     def call(self):
#         demo.__display()
# obj=demo()
# obj.call()


#doc string comment
# def demo():
#     ''' this is  comment line      ,kkhh'''
# print(demo.__doc__)



#generator

def demo():
    name ="Kalai"
    age = 23
    yield name
    yield age
    yield age
x = demo()
print(x.__next__())
print(next(x))






















