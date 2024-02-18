from database.database import Database
from tkinter import Tk, Label, Entry, Button


def show_message(message):
    info = Label(root, text=message)
    info.pack()

def validate_data():
    if db.search_data(login_entry.get(), password_entry.get()):
        show_message("Login successful")
    elif not db.search_data(login_entry.get(), password_entry.get()):
        show_message("Invalid password")
    else:
        show_message("Successfully sign-up")


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
# Database setting
name = 'demo'
user = 'postgres'
password = '123'
host = 'localhost'
port = '5432'
db = Database(database_name=name, database_user=user,
              database_password=password, database_host=host,
              database_port=port)
button_password = Button(text="validate", bg='azure2',
                         command=lambda: validate_data())
button_password.pack()

root.mainloop()
