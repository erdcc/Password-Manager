#!/usr/bin/env python3
import tkinter as tk
import random
import string
import sqlite3


def close():
    con.close()
    win.destroy()


win = tk.Tk()
win.protocol("WM_DELETE_WINDOW", close)
win.title("Password Manager")
win.geometry("450x250+500+200")

# Grid form
app = tk.Frame(win)
app.grid()

# starting database
con = sqlite3.connect("database.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS passwords(application TEXT, username TEXT, password TEXT)")


# Functions
def AddFunc():
    try:
        cursor.execute("INSERT INTO PASSWORDS VALUES(?,?,?)", (txtApp.get(), txtUsername.get(), txtPassword.get(),))
        con.commit()
        lblMessage.config(text="Password is added successfully")
    except sqlite3.IntegrityError:
        lblMessage.config(text="Application has been already added.")


def EditFunc():
    cursor.execute("UPDATE PASSWORDS SET USERNAME=?, PASSWORD=? WHERE APPLICATION =?",
                   (txtUsername.get(), txtPassword.get(), txtApp.get(),))
    con.commit()
    lblMessage.config(text="Editing is done.")


def ShowFunc(event):
    txtPassword.delete(0, 'end')
    txtUsername.delete(0, 'end')
    lblMessage.config(text="")
    try:
        cursor.execute("SELECT USERNAME,PASSWORD FROM PASSWORDS WHERE APPLICATION=?", (txtApp.get(),))
        data = cursor.fetchall()
        txtUsername.insert(0, data[0][0])
        txtPassword.insert(0, data[0][1])
    except:
        lblMessage.config(text="ERROR,There is no application!")


def RandomFunc():
    txtPassword.delete(0, 'end')
    password_characters = string.ascii_letters + string.digits + "!#$%&-/<=>?@\\}_"
    random_password = random.choices(password_characters, k=10)
    password = ''.join(random_password)
    txtPassword.insert(0, password)


def CopyNameFunc():
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(txtUsername.get())
    r.update()
    r.destroy()
    lblMessage.config(text="Copied to Clipboard")


def CopyPassFunc():
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(txtPassword.get())
    r.update()
    r.destroy()
    lblMessage.config(text="Copied to Clipboard")


def DeleteFunc():
    cursor.execute("DELETE FROM PASSWORDS WHERE APPLICATION=?", (txtApp.get(),))
    lblMessage.config(text="Password is deleted.")
    con.commit()


def listApps(event):
    popup = tk.Toplevel()
    popup.wm_title("Application List")
    cursor.execute("SELECT APPLICATION FROM PASSWORDS")
    apps = cursor.fetchall()
    for i in range(len(apps)):
        t = tk.Label(popup, text=apps[i])
        t.grid(row=i, column=1)


# initializing objects
lblApp = tk.Label(app, text="Application : ")
txtApp = tk.Entry(app, bg="white", bd=2, font="TimesNewRoman 12 bold", fg="black")
txtApp.bind("<Double-Button-1>", listApps)
txtApp.bind('<Return>', ShowFunc)

lblUsername = tk.Label(app, text="Username : ")
txtUsername = tk.Entry(app, bg="white", bd=2, font="Arial 12 bold", fg="black")

lblPassword = tk.Label(app, text="Password : ")
txtPassword = tk.Entry(app, bg="white", bd=2, font="TimesNewRoman 12 bold", fg="black")
lblMessage = tk.Label(app, text="")

btnAdd = tk.Button(app, text="Add", command=AddFunc)
btnEdit = tk.Button(app, text="Edit", command=EditFunc)
btnShow = tk.Button(app, text="Show", command=ShowFunc)
btnRandomPass = tk.Button(app, text="Create Random Password", command=RandomFunc)
btnCopyName = tk.Button(app, text="Copy to Clipboard", command=CopyNameFunc)
btnCopyPass = tk.Button(app, text="Copy to Clipboard", command=CopyPassFunc)
btnDelete = tk.Button(app, text="Delete", command=DeleteFunc)

# position of objects
lblApp.grid(row=0, column=0, padx=5, pady=5, sticky="E")  # Sağa hizalı (sticky = "E")
txtApp.grid(row=0, column=1, padx=5, pady=5, sticky="W")  # Sola hizalı (sticky = "W")

lblUsername.grid(row=1, column=0, padx=5, pady=5, sticky="E")  # Sağa hizalı (sticky = "E")
txtUsername.grid(row=1, column=1, padx=5, pady=5, sticky="W")  # Sola hizalı (sticky = "W")

lblPassword.grid(row=2, column=0, padx=5, pady=5, sticky="E")
txtPassword.grid(row=2, column=1, padx=5, pady=5, sticky="W")

lblMessage.grid(row=5, column=1, padx=5, pady=5, sticky="S")

btnEdit.grid(row=3, column=0, columnspan=1, padx=1, pady=5)
btnDelete.grid(row=4, column=0, columnspan=1, padx=1, pady=5)
btnAdd.grid(row=3, column=1, columnspan=1, padx=1, pady=5)
btnShow.grid(row=0, column=2, columnspan=1, padx=1, pady=5)
btnRandomPass.grid(row=4, columnspan=4, padx=1, pady=5)
btnCopyName.grid(row=1, column=2, columnspan=1, padx=1, pady=5)
btnCopyPass.grid(row=2, column=2, columnspan=1, padx=1, pady=5)

# Plot form
win.mainloop()
