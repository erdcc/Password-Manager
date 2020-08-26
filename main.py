import tkinter as tk
import random
import string
import sys,os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2",os.path.abspath("."))

    return os.path.join(base_path, relative_path)

class Password:
    def __init__(self,a):
        self.app,self.user,self.password=a

    def __del__(self):
        print("deleted")

    def add_pass(self):
        list.append(self)

    def read_pass(self):
        print("application: "+self.app+" username: "+self.user+" password: "+self.password)

    def edit_pass(self,a,b):
        self.user=a
        self.password=b

list=[]

with open(resource_path('pass.txt')) as f:
    for line in f:
        if not line.strip(): continue  # skip the empty line
        list.append(Password(line.split(",")))


def close():
    file = open(resource_path('pass.txt'), "w")
    for a in list:
        file.write(a.app + "," + a.user + "," + a.password+"\n")
    file.close()
    win.destroy()

if __name__ == '__main__':

    win = tk.Tk()
    win.protocol("WM_DELETE_WINDOW", close)
    win.title("Password Manager")
    win.geometry("400x220+500+200")

    # Formu grid olarak çizdirme /layout düzeni
    app = tk.Frame(win)
    app.grid()


    # Fonksiyonlar
    def AddFunc():
        hata=False
        for a in list:
            if  txtApp.get() == a.app:
                lblMessage.config(text="Application has been already added.")
                hata=True
                break
        if hata is not True:
            Password((txtApp.get(),txtUsername.get(),txtPassword.get())).add_pass()
            lblMessage.config(text="Password is added successfully")
    def EditFunc():
        for a in list:
            if txtApp.get() == a.app:
                a.edit_pass(txtUsername.get(), txtPassword.get())
                lblMessage.config(text="Editing is done.")



    def ShowFunc():
        txtPassword.delete(0, 'end')
        txtUsername.delete(0, 'end')
        lblMessage.config(text="")
        for a in list:
            if txtApp.get()==a.app:
                txtUsername.insert(0, a.user)
                txtPassword.insert(0, a.password)
        if txtUsername.get()== "" and txtPassword.get()=="" :
            lblMessage.config(text="ERROR,There is no application!")


    def RandomFunc():
        txtPassword.delete(0, 'end')
        password_characters = string.ascii_letters + string.digits + "!#$%&-/<=>?@\_"
        password = ''.join(random.choice(password_characters) for i in range(10))
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
        for a in list:
            if txtApp.get()==a.app:
                list.remove(a)
                lblMessage.config(text="Password is deleted.")
                txtApp.delete(0, 'end')
                txtUsername.delete(0, 'end')
                txtPassword.delete(0, 'end')

    def applist(event):
        popup = tk.Toplevel()
        popup.wm_title("Application List")
        for i in range(len(list)):
            l = tk.Label(popup, text=list[i].app)
            l.grid(row=i, column=1)


    lblApp = tk.Label(app, text="Application : ")
    txtApp = tk.Entry(app, bg="white", bd=2, font="TimesNewRoman 12 bold", fg="black")
    txtApp.bind("<Double-Button-1>", applist)

    lblUsername = tk.Label(app, text="Username : ")
    txtUsername = tk.Entry(app, bg="white", bd=2, font="Arial 12 bold", fg="black")

    lblPassword = tk.Label(app, text="Password : ")
    txtPassword = tk.Entry(app, bg="white", bd=2, font="Arial 12 bold", fg="black")
    lblMessage  = tk.Label(app,text="")

    btnAdd = tk.Button(app, text="Add", command=AddFunc)
    btnEdit = tk.Button(app, text="Edit", command=EditFunc)
    btnShow = tk.Button(app, text="Show", command=ShowFunc)
    btnRandomPass = tk.Button(app, text="Create Random Password", command=RandomFunc)
    btnCopyName = tk.Button(app, text="Copy to Clipboard", command=CopyNameFunc)
    btnCopyPass = tk.Button(app, text="Copy to Clipboard", command=CopyPassFunc)
    btnDelete = tk.Button(app, text="Delete", command=DeleteFunc)


    # Herbir nesnenin ekrandaki yerini belirle
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

    # Formu çiz

    win.mainloop()

