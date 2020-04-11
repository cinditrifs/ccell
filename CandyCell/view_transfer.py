from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import redis
from tkinter import messagebox


ccell = redis.Redis(
           host='127.0.0.1',
           port=6379, db='1')

class transaksi :
    '''def __init__(self) :
        self.root = Tk()
        self.transaksi(self.root)
              

    def transaksi (self, root):'''
    def __init__ (self,root):
        self.master= root
        self.master.title("TRANSAKSI")
        self.master.geometry("500x500+350+120")
        self.master.config(bg="lightskyblue2")

        self.title=Label(self.master, text="TRANSAKSI", font=(
                        "times new roman", 18, "bold"), bg="white",
                         fg="deepskyblue3", bd=10)     
        self.title.place(x=0, y=40, relwidth=1)

        #meletakkan entri
        self.frame= Frame(self.master)
        self.frame.place(x= 150, y=130)
       
        txt1 = Label(self.frame, text = 'Masukkan Nomor HP', font = ('consolas', 12, "bold")
                         , fg = "blue4")
        txt1.grid (row = 0, column = 0)
        user_entry = Entry(self.frame, width = 40,)
        user_entry.grid (row = 1, column = 0)
        
        txt2 = Label(self.frame, text = 'Sejumlah', font = ('consolas', 12, "bold")
                         , fg = "blue4")
        txt2.grid (row = 2, column = 0)
        user_entry = Entry(self.frame, width = 40)
        user_entry.grid (row = 3, column = 0)

        txt3 = Label(self.frame, text = 'Masukkan Password', font = ('consolas', 12, "bold")
                         , fg = "blue4")
        txt3.grid (row = 4, column = 0)
        user_entry = Entry(self.frame, width = 40, show= "*")
        user_entry.grid (row = 5, column = 0)

        button = Button(self.frame, width =10, text = "kirim", command=
                        self.info)
        button.grid(row=6, column=0)

    def info (self):
        messagebox.showinfo("info", "sedang dalam proses")
'''        
#kode_paket = StringVar()

#kode_paket=input(str('masukkan kode Paket:'))

#detail = ccell.hmget(kode_paket, 'detail')
#harga = ccell.hmget(kode_paket, 'harga')
#print (harga)
#print(detail)
if __name__ == '__main__':
    transaksi()'''

