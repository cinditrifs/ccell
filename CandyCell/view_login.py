from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
from view_admin_manage import main_menu_admin as main_menu_admin
from view_agen_manage import main_menu_agen as main_menu_agen

import redis
ccell = redis.Redis(
           host='127.0.0.1',
           port=6379, db=1)

class login_admin :
    def __init__(self, root) : 
        self.master = root
        self.master.title("LOGIN SYSTEM")
        self.master.geometry("500x500+350+120")
        self.master.config(bg="lightskyblue2")

        self.title=Label(self.master, text="SILAHKAN LOGIN", font=(
                        "times new roman", 18, "bold"), bg="white",
                         fg="deepskyblue3", bd=10)     
        self.title.place(x=0, y=40, relwidth=1)

        #buat frame login
        self.frame_login = LabelFrame(self.master, height = 200, width= 200)
        self.frame_login.place(x=50, y=160)

        #meletakkan entri dan button login
        self.username = StringVar()
        self.password = StringVar()
        
        user_txt = Label(self.frame_login, text = "USERNAME", font = ('consolas', 12, "bold")
                         , fg = "blue4")
        user_txt.grid (row = 0, column = 0)
        user_entry = Entry(self.frame_login, width = 60, textvariable = self.username)
        user_entry.grid (row = 1, column = 0)
        
        pass_txt = Label(self.frame_login, text = "PASSWORD", font = ('consolas', 12, "bold")
                         , fg = "blue4")
        pass_txt.grid (row = 3, column = 0)
        pass_entry = Entry(self.frame_login, width = 60,textvariable = self.password, show = "*" )
        pass_entry.grid (row = 4, column = 0)
        
        button = Button(self.frame_login, text = "login", width = 4, height =1
                       , command = self.auth) 
        button.grid(row= 6, column = 0)
        
    def auth (self):
        key = self.username.get()
        password = self.password.get()
        #print (type(password))
        pass_auth = (str(ccell.hmget(key, 'password'))).replace('b','')
        pass_auth = pass_auth.replace(']', '')
        pass_auth = pass_auth.replace('[', '')
        pass_auth = pass_auth.replace("'", '')
        #print(type(pass_auth))
        if password == pass_auth :
            self.auth = Toplevel(self.master)
            self.app= main_menu_admin(self.auth)
        else :
            messagebox.showinfo("failed", "Usename dan Password tidak sama")

 
class login_agen :
    def __init__(self, root) :
        self.master = root
        self.master.title("LOGIN SYSTEM")
        self.master.geometry("500x500+350+120")
        self.master.config(bg="lightskyblue2")

        self.title=Label(self.master, text="SILAHKAN LOGIN", font=(
                        "times new roman", 18, "bold"), bg="white",
                         fg="deepskyblue3", bd=10)     
        self.title.place(x=0, y=40, relwidth=1)

        #buat frame login
        self.frame_login = LabelFrame(self.master, height = 200, width= 200)
        self.frame_login.place(x=50, y=160)

        #meletakkan entri dan button login
        self.id = StringVar()
        self.pin_agen = StringVar()
        user_txt = Label(self.frame_login, text = "ID AGEN", font = ('consolas', 12, "bold")
                         , fg = "blue4")
        user_txt.grid (row = 0, column = 0)
        user_entry = Entry(self.frame_login, width = 60, textvariable = self.id)
        user_entry.grid (row = 1, column = 0)
        
        pass_txt = Label(self.frame_login, text = "PIN AGEN", font = ('consolas', 12, "bold")
                         , fg = "blue4")
        pass_txt.grid (row = 3, column = 0)
        pass_entry = Entry(self.frame_login, width = 60,textvariable = self.pin_agen, show = "*" )
        pass_entry.grid (row = 4, column = 0)
        
        button = Button(self.frame_login, text = "login", width = 4, height =1
                       , command = self.auth) 
        button.grid(row= 6, column = 0)
        
   
        button = Button(self.frame_login, text = "login", width = 4, height =1, command = self.auth) 
        button.grid(row= 6, column = 0)
        
    def auth (self):
        key = self.id.get() #nanti di db ubah samain kayak key
        pin = self.pin_agen.get()
        #print (type(pin))
        pass_auth = (str(ccell.hmget(key, 'pin'))).replace('b','')
        pass_auth = pass_auth.replace(']', '')
        pass_auth = pass_auth.replace('[', '')
        pass_auth = pass_auth.replace("'", '')
        #print(pass_auth)
        if pin == pass_auth :
            self.auth = Toplevel(self.master)
            self.app= main_menu_agen(self.auth)
        else :
            messagebox.showinfo("failed", "Usename dan Password tidak sama")



