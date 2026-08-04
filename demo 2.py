'''
#special operators

#identity operators

#Example:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # is not
print(x is y) #false
print(x == y)

print( x is not y) #true


#membership operators

x = ["apple", "banana"]
print("banana" in x) #true

x = ["apple", "banana"]
print("pineapple" not in x ) #true


z = ["apple", "banana"]
print("Banana" in z) #false



#IF STATEMENT

x=25
if x>=23:
    print('Correct')
else:
    print('wrong')


a=18
b=23
if a>b:
    print('b is greater')
else:
    print('a is smaller')


a=int(input('Enter Your Marks'))
if a>=40:
    print('PASS')
else:
    print('FAIL')



#elif ladder


a=20
b=10
c=30
if a<b:
    print('1st')
elif a>b:
    print('2nd')
elif b<c:
    print('3rd')
else:
    print('NO')



#grade system

a=int(input("Enter a Mark:"))
if a>90:
    print('S Grade')
elif a>80:
    print('A Grade')
elif a>70:
    print('B Grade')
elif a>60:
    print('C Grade')
elif a>=50:
    print('D Grade')
else:
    print('Fail')




#nested if-else


a=10
b=20
c=30
if a<b:
    print(a)
    if a>c:
        print(b)
    else:
        print(c)
else:
    print(c)	





#exam system


m1=int(input("Enter The Marks 1:"))
if m1>80:
    print("Test 1 Passed")
    m2=int(input("Enter The Marks 2:"))
    if m2>75:
        print("Test 2 Passed")
        m3=int(input("Enter The Marks 3:"))
        if m3>90:
            print("Cleared the Exams")
        else:
            print("Test 3 Failed")
    else:
        print("Test 2 Failed")
else:
    print("Test 1 failed")


'''

#insta login page

    
username=input("Enter Ur UserName:")
if username=="kalai@gmail.com":
    pwd=int(input("Enter Ur Password:"))
    if pwd==1234:
        print("Login Successfull")
    else:
        print("Password Incorrect")
else:
    print("Enter ur username correctly")
    
    
          
          
          







