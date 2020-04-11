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
    def __init__(self, root) :
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
        self.kode_paket = StringVar()
        self.detail =StringVar()
       
        txt1 = Label(self.frame, text = 'kode paket', font = ('consolas', 12, "bold")
                         , fg = "blue4")
        txt1.grid (row = 0, column = 0)
        user_entry = Entry(self.frame, width = 40, textvariable = self.kode_paket)
        user_entry.grid (row = 1, column = 0)
        button = Button(self.frame, text = "oke", width = 4, height =1 ,
                        command = self.detail) 
        button.grid(row= 2, column = 0)
        txt2 = Label(self.frame, text = 'detail dan harga', font = ('consolas', 12, "bold")
                         , fg = "blue4")
        txt2.grid (row = 3, column = 0)
        detailLabel = Label(self.frame, textvariable= self.detail)
        detailLabel.grid(row=4, column=0)
        self.detail.set('detail')
        
        txt3 = Label(self.frame, text = 'ke nomor', font = ('consolas', 12, "bold")
                         , fg = "blue4")
        txt3.grid (row = 5, column = 0)

        user_entry = Entry(self.frame, width = 40)
        user_entry.grid (row = 6, column = 0)

        button = Button(self.frame, text = "kirim", width = 4, height =1 ,
                        command = self.info) 
        button.grid(row= 7, column = 0)
        
        def detail (self, key) :
            key = self.kode_paket.get()
            detail = str(ccell.hmget(key, "detail"))
            detail = print(detail)
            price = ccell.hmget(key, 'harga')
            print(key, detail, price)

            self.detail.set(detail)
    def info (self) :
       messagebox.showinfo("info", "sedang dalam proses")


#kode_paket = StringVar()

#kode_paket=input(str('masukkan kode Paket:'))

#detail = ccell.hmget(kode_paket, 'detail')
#harga = ccell.hmget(kode_paket, 'harga')
#print (harga)
#print(detail)
'''if __name__ == '__main__':
    transaksi()'''
