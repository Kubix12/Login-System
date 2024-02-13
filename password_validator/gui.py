from tkinter import *
from hashpassword import Login

root = Tk()
root.geometry('300x300')
root.configure(background='black')

# login
text = Label(root, text='Entry nick', bg='black', fg='azure')
text.pack()
login_entry = Entry(bg='black', fg='azure')
login_entry.pack()

# password
text_password = Label(root, text='Entry password', bg='black', fg='azure')
text_password.pack()
password_entry = Entry(root, bg='black', fg='azure')
password_entry.pack()
button_password = Button(text="validate", bg='azure2',
                         command=lambda: Login.validate_data(login_entry.get(), password_entry.get()))
button_password.pack()

root.mainloop()
