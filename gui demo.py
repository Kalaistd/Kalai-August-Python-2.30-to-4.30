from tkinter import *
from tkinter import messagebox, scrolledtext
from tkinter.ttk import Combobox


# Create Window
tab = Tk()
tab.title("Demo Application")
tab.geometry("700x600")
tab.configure(bg="white")

# Function for Button Action
def click_me():
    lbl_result.config(text=f"Welcome {txt_name.get()}")

# Function for Submit Button
def submit():
    name = txt_name.get()
    department = dept.get()
    age_value = age.get()
    gender = gender_var.get()

    messagebox.showinfo(
        "Details Submitted",
        f"Name: {name}\nDepartment: {department}\nAge: {age_value}\nGender: {gender}"
    )

    sct.insert(
        END,
        f"Name: {name}, Department: {department}, Age: {age_value}, Gender: {gender}\n"
    )

# Labels
Label(tab, text="Name", font=("Arial", 14),
      bg="GREY").place(x=50, y=50)

# Entry Widget
txt_name = Entry(tab, width=45)
txt_name.place(x=180, y=50)

# Combobox
Label(tab, text="Department", font=("Arial", 14),
      bg="white").place(x=50, y=100)

dept = Combobox(tab, width=22)
dept["values"] = ("Select", "CSE", "ECE", "EEE", "MECH")
dept.current(0)
dept.place(x=180, y=100)

# Spinbox
Label(tab, text="Age", font=("Arial", 14),
      bg="white").place(x=50, y=150)
#
age = Spinbox(tab, from_=18, to=25, width=20)
age.place(x=180, y=150)

# Radiobuttons
Label(tab, text="Gender", font=("Arial", 14),
      bg="white").place(x=50, y=200)

gender_var = StringVar()
gender_var.set("Male")

rb1 = Radiobutton(tab, text="Male",
                  variable=gender_var,
                  value="Male",
                  bg="white")
rb1.place(x=180, y=200)

rb2 = Radiobutton(tab, text="Female",
                  variable=gender_var,
                  value="Female",
                  bg="white")
rb2.place(x=260, y=200)

# Click Me Button
btn_click = Button(
    tab,
    text="Click Me ",
    fg="white",
    bg="brown",
    command=click_me
)
btn_click.place(x=180, y=250)

# Result Label
lbl_result = Label(tab, text="", font=("Arial", 12), bg="white")
lbl_result.place(x=280, y=255)

# Submit Button
btn_submit = Button(
    tab,
    text="Submit",
    bg="green",
    fg="white",
    command=submit
)
btn_submit.place(x=180, y=300)

# Scrolled Text
Label(tab, text="Output", font=("Arial", 14),
      bg="red").place(x=50, y=350)

sct = scrolledtext.ScrolledText(tab, width=50, height=10)
sct.place(x=50, y=390)

# Close Button
btn_close = Button(
    tab,
    text="Close",
    bg="red",
    fg="white",
    command=tab.destroy
)
btn_close.place(x=280, y=300)

tab.mainloop()
