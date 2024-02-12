from tkinter import *
from hashpassword import Login


root = Tk()
root.geometry('300x300')

# login
text = Label(root, text='Entry nick')
text.pack()
login_entry = Entry()
login_entry.pack()
button_login = Button(text="validate", command=lambda: Login.validate_nick(login_entry.get()))
button_login.pack()

# password
text_password = Label(root, text='Entry password')
text_password.pack()
password_entry = Entry(root)
password_entry.pack()
button_password = Button(text="validate", command=lambda: Login.validate_password(password_entry.get()))
button_password.pack()


root.mainloop()
