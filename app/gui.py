
import sqlite3
import tkinter as tk
from tkinter.ttk import *

def create_db():
    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS person (username TEXT, password TEXT);')
    conn.commit()
    conn.close()

def save_data(user, password):

  if user and password:

    conn = sqlite3.connect('person.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO person (username, password) VALUES (?, ?)', (username_entry.get(), password_entry.get()))
    conn.commit()
    conn.close()
    top = tk.Toplevel(alert)
    top.geometry('200x200')
    top.title("User Register APP")
    label = tk.Label(top, text="Successful registered user.")
    label.pack(pady=(80, 0))
    label.pack()

  else:

    top = tk.Toplevel(alert)
    top.geometry('200x200')
    top.title("User Register APP")
    label = tk.Label(top, text="Incorrect user or password.")
    label.pack(pady=(80, 0))
    label.pack()

root = tk.Tk()
root.title('User Register APP')
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
create_db()

f1, f2, f3, alert = Frame(root), Frame(root), Frame(root), Frame(root)

for frame in (f1, f2, f3, alert):
  frame.grid(row=0, column=0, sticky='nsew')

# username
user_get = tk.StringVar()
username_label = Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = Entry(root, textvariable=user_get)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_get = tk.StringVar()
password_label = Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_entry = Entry(root,  show="*", textvariable=password_get)
password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = Button(root, text="Register", command=lambda:save_data(user=username_entry.get(), password=password_entry.get()))
login_button.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

root.mainloop()