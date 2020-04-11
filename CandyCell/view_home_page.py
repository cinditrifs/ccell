from tkinter import *
import tkinter.messagebox
from tkinter import ttk
#from view_login import login_admin as window_login_admin
#from view_login import login_agen as window_login_agen
import view_login


class home_page : #menu awal
    def __init__ (self) :
        self.root = Tk()
        self.mulai(self.root)

    def mulai (self, root):
        self.master= root
        self.master.title("CANDY CELL")
        self.master.geometry("500x500+350+120")
        self.master.config(bg="deepskyblue3")

        self.title = Label(self.master, text = "SELAMAT DATANG DI CANDY SELULAR",
                            font = ("Times new roman", 15, 'bold'), bg = "white", fg = "deepskyblue3")
        self.title.place(x= 50, y= 30)

        #buat frame user
        
        self.frame_admin = LabelFrame(self.master, height = 80, width= 40)
        self.frame_admin.place(x=160, y=150)
        
        #meletakkan button user
        self.tombol_admin = Button(self.frame_admin, text = 'ADMIN',
                                   width = 8, height =8, command= self.new_window_admin)
        self.tombol_admin.grid(row =0,  column=0, padx= 10, pady= 10)
        self.tombol_agen = Button(self.frame_admin, text = 'AGEN',
                                   width = 8, height =8, command= self.new_window_agen)
        self.tombol_agen.grid(row=0, column=1, padx= 10, pady= 10)
        
    def new_window_admin (self) :
        self.new_window_admin = Toplevel(self.master)
        self.app=view_login.login_admin(self.new_window_admin)

    def new_window_agen (self) :
        self.new_window_agen = Toplevel(self.master)
        self.app = view_login.login_agen(self.new_window_agen)
        
#if __name__ == '__main__':
 #   home_page()
    
