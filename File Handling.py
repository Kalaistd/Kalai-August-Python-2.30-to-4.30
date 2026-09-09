# # Create a new file
# a=open(r"C:\Users\ELCOT\Desktop\aaaa.txt","x")

#write
# Write a file
# a=open("C:/Users/ELCOT/Desktop/aaaa.txt","w")
# a.write("I love India")
# a.close()
# print("success")

# Append a file
# a=open("C:/Users/ELCOT/Desktop/aaaa.txt","a")
# a.write("I love India")
# a.close()
# print("success")


# Read a file
# a=open("C:/Users/ELCOT/Desktop/aaaa.txt","r")
# print(a.read())
# #To print all lines in to the file
# print(a.readline())
# #To read a file into line by line
# print(a.read(3))


# To delete a file
# import os
# os.remove("C:/Users/ELCOT/Desktop/aaaa.txt")


# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# plt.plot(xpoints, ypoints)
# plt.show()


#exception handling

# try:
#     x=10
#     print(y)
# except Exception as e :
#     print(e)
# finally:
#     print("operation  done")


#Raise
# Example for raise

# try:
#     a=int(input("enter a num"))
#     b=int(input('enter a num'))
#     if b==0:
#         raise ZeroDivisionError('value should not be zero')
#     c=a+b
#     d=a-b
#     e=a/b
#     print(c,d,e)
# except Exception as e:
#     print(e)
# finally:
#     print("operation done")


#Assert
# 1.Example for assert
# x="hello"
# assert x=="Hai"
# print(x)

# 2.Example for assert
x="hello"
assert x=="hello"
print(x)













