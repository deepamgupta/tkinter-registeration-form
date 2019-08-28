import tkinter as tk
import sqlite3 as s

w = tk.Tk()
w.title("Student")

db = s.connect('my.db')

name = tk.StringVar()
email = tk.StringVar()


def insert():
    db.execute('Insert into Student values ("'+name.get()+'","'+email.get()+'");')
    db.commit()


nameLabel = tk.Label(w,text="Name : ")
nameLabel.grid(row=0, column=0)

nameEntry = tk.Entry(w, textvar = name)
nameEntry.grid(row = 0, column = 1)

emailLabel = tk.Label(w, text="Email : ")
emailLabel.grid(row = 1, column = 0)

emailEntry = tk.Entry(w, textvar = email)
emailEntry.grid(row = 1, column = 1)

submit = tk.Button(w, text = "Submit", command = insert)
submit.grid(row = 2, column = 0)
w.mainloop()

db.close()