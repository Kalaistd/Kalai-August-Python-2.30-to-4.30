# # #create
# aa=open(r"C:\Users\ELCOT\Desktop\kalai.txt","x")

#write
aa=open(r"C:\Users\ELCOT\Desktop\kalai.txt","w")
aa.write("Hello All!")
aa.close()
print("Success")

# # #append
aa=open(r"C:\Users\ELCOT\Desktop\kalai.txt","a")
aa.write("Good Morning...")
aa.close()
print("Append Success")

#read
aa=open(r"C:\Users\ELCOT\Desktop\kalai.txt","r")
print(aa.read())
#To print all lines in to the file
# print(aa.readline())
# #To read a file into line by line
# print(aa.read(3))


#remove
# import os
# os.remove(r"C:\Users\ELCOT\Desktop\kalai.txt")