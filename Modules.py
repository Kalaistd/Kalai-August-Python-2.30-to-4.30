# Predefined modules
# 1.Math
# import math
# print(math.pi)#3.1415
# print(math.ceil(7.3))#8
# print(math.floor(7.2))
# print(math.factorial(13))#120
# print(math.sqrt(25))#5.0
# print(math.pow(2,3))
# print(math.sin(0))
# # print(m.pi)


# 2.Scipy (Scientific python)
# from scipy import constants as c
# print(c.gram)#0.001
# print(c.milli)#0.001
# print(c.hour)#3600.0
# print(c.degree)#0.017453292519943295
# print(c.pound)#0.45359236999999997
# print(c.year)#31536000.0
# print(c.day)#86400.0
# print(c.kilo)
# print(c.kilogram)

# 3.Time
# import time
# print(time.ctime())#Fri Sep  1 11:21:41 2023
# print("hii")
# time.sleep(3)
# print("hello")


# 4.calendar
# import calendar as c
# print(c.month(2026,8))
# print(c.isleap(2024))
# print(c.calendar(2030))


# 5. datetime
# import datetime as d
# print(d.datetime.now())

# 6.Numpy(numeric python)
# import numpy as m
# a=m.array([3,1,2,5,4,6])
# print(a)
# print(type(a))
# print(m.min(a))
# print(m.shape(a))
# print(m.max(a))
# print(m.sqrt(a))
# print(m.mean(a))
# print(m.median(a))


# Pandas
#read csv files
# import pandas as pd
# df = pd.read_csv('C:/Users/ELCOT/Downloads/users.csv')
# print(df.to_string())

# dd= pd.read_excel(r'C:\Users\ELCOT\Downloads\Finalized 250 Students list.csv')
# print(dd.to_string())

#for series
# import pandas as pd
a=[10, 20, 30, 40]
# s = pd.Series(a)
# print(s)


#dataframe
# data = {
# 	"Name": ["John", "Alice", "Bob"],
# 	"Age": [25, 30, 22]
# }
# df = pd.DataFrame(data)
# print(df)

# Matplotlib

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([0,3,6,9,10])
# y = np.array([50,74,138,29,250])
#
# plt.plot(x, y)
# plt.xlabel('Age')
# plt.ylabel('Salary')
# plt.show()


import matplotlib.pyplot as plt
# subjects = ["Math", "Science", "English"]
# marks = [90, 85, 95]
# plt.bar(subjects, marks)
# plt.title("Student Marks")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()



# subjects = ["Math", "Science", "English"]
# marks = [90, 85, 95]
# plt.pie(marks)
# plt.title("Subjects")
# plt.show()
# plt.show()

# 7.pywhatkit
# import pywhatkit as kit
# kit.search("Apple")


#for scheduled msg
# kit.sendwhatmsg("+917200111681","Hello World!",1,30)
#for instant msg
# kit.sendwhatmsg_instantly("+91720011681","Hello!")
#for play an youtube
# kit.playonyt("Cherry Pie")


# 8. webbrowser
# import webbrowser
# webbrowser.open_new_tab("https://www.youtube.com/watch?v=5oH9Nr3bKfw")


# 9.socket
import socket
host=socket.gethostname()
host
# 'LAPTOP-91BD0SRS’

