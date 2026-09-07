# 6.Numpy(numeric python)
# import numpy as m
# a=m.array([1,2,3,4,5])
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
# df = pd.read_csv(r'C:\Users\ELCOT\Downloads\PurchaseOrders.csv')
# print(df.to_string())


#for series
# import pandas as pd
# a=[10, 20, 30, 40]
# s = pd.Series(a)
# print(s)
#
# #dataframe
# import pandas as pd
# data = {
# 	"Name": ["John", "Alice", "Bob","Shambavi"],
# 	"Age": [25, 30, 22, 18]
# }
# df = pd.DataFrame(data)
# print(df)


# # Matplotlib

# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([1,3,7,13,18,23])
# ypoints = np.array([12,33,3,18,66,89])
# plt.plot(xpoints, ypoints)
# plt.xlabel('Age')
# plt.ylabel("Marks")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([1,3,7,13,18,23])
# ypoints = np.array([12,33,3,18,66,89])
#
# plt.bar(xpoints, ypoints)
# plt.xlabel('Age')
# plt.ylabel("Marks")
# plt.show()
#
# import matplotlib.pyplot as plt
# subjects = ["Math", "Science", "English"]
# marks = [90, 65, 95]
# plt.plot(subjects, marks)
# plt.xlabel("Subjects")
# plt.ylabel("Students Marks")
# plt.title("Student Marks")
# plt.show()

############################################

# 7.pywhatkit
import pywhatkit as kit
# kit.search("livewire")


#for scheduled msg
# kit.sendwhatmsg("+918124772380","Hello Gowsik!",10,1)
#for instant msg
# kit.sendwhatmsg_instantly("+918124772380","Hello Gowsik!")
#for play an youtube
# kit.playonyt("cocomelon")


# 8. webbrowser
import webbrowser
webbrowser.open_new_tab("https://www.youtube.com/watch?v=5oH9Nr3bKfw")
















