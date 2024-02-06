from tkinter import *
from hashpassword import Password


root = Tk()
root.geometry('300x300')

password_entry = Entry(root)
password_entry.pack()
button = Button(text="validate", command=lambda: Password.validate(password_entry.get()))
button.pack()


root.mainloop()
