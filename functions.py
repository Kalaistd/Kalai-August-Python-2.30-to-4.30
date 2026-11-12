#functions

# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# add()
#
# a=100
#
# #without args
# def addd():
#     a=int(input("Enter a number:"))
#     b=int(input("Enter a number:"))
#     c=a*b
#     print(c)
# addd()
# print(a)
#
# add()

#with args
# print("----------")
# def sub(a,b):
#     c=a-b
#     print("sub value",c)
# sub(23,5)

#positional args

# def div(b,a):
#     c=a/b
#     print('div value',c)
# div(25,5)


#default args

# def add(a,b=3):
#     c=a+b
#     print('add value',c)
# add(23)
# add(23,10)


#positional args
# print('---------------------')
# def function(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# function(30,20)

#default args
# def student(name,age=18):
#     print("student name:",name)
#     print("student age:",age)
# student("Shambavi",23)


# Example for keyword argument
# def demo(**p):
#     for i,j in p.items():
#         print(type(p))
#         print(i,j)
# demo(a=10,b=12,c=22,d=23)


# def greet(name,age):
#     print(f"I'm {name} and {age} years old")
# greet(age=25,name="Dinesh")

#variable args
# def demo(*p):
#     for i in p:
#         print(type(p))
#         print(i)
# demo("a",10,"b",12,"c",22,"d",23)


#passing a list as args
# def concat(fn,ln):
#     s = f"{fn}{ln}"
#     return s
# print(concat("Kalai", "Selvan"))
#
#
# full_name = concat("Praveen", "Kumar")
# print(full_name)


#return
# def demo(x):
#     return 5*x
# # print(demo(10))
# print(demo('hi'))



# RECURSIVE FUNCTION:
# Function : function can call itself.
# # Example:
# def fact(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n * fact(n - 1)  # Recursive call
#
# print(fact(4))

#lambda fns
a=lambda c , d : c + d
print(a(10,20))
