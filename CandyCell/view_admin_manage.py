from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import redis
import view_daftar_agen
import view_daftar_paket
import view_transfer

'''def mulai():
    root = Tk()
    app = main_menu_admin (root)'''

class main_menu_admin :
    def __init__(self, root) : 
        self.master = root
        self.master.title("MAIN MENU")
        self.master.geometry("500x500+350+120")
        self.master.config(bg="lightskyblue2")

        #buat bikin tombol keluar
        tool = Menu(self.master, tearoff = 0)
        tool.add_cascade(label="...", menu = tool)
        tool.add_command(label= "exit")
    
        self.title=Label(self.master, text="CANDYSELL", font=(
                        "times new roman", 10, "bold"), bg="white",
                         fg="deepskyblue3", bd=10)     
        self.title.place(x=2, y=1, relwidth = 1)

        #buat frame menu
        self.frame_menu = LabelFrame(self.master, height = 30, width = 40)
        self.frame_menu.place (x= 20, y = 150)

        #meletakkan button menu
        self.tombol_daftar_agen = Button(self.frame_menu, text = "Daftar Agen",
                                         width = 15, height =8,
                                         command = self.to_daftar_agen)
        self.tombol_daftar_agen.grid(row =0, column =0)
        
        self.tombol_daftar_harga = Button(self.frame_menu, text = "Daftar Harga",
                                         command= self.to_daftar_paket,
                                         width = 15, height =8)
        self.tombol_daftar_harga.grid(row =0, column =1)

        self.tombol_riwayat_transaksi = Button(self.frame_menu, text = "Riwayat Transaksi",
                                         width = 15, height =8,
                                        command = self.info)
        self.tombol_riwayat_transaksi.grid(row =1, column =0)

        self.tombol_kirim_saldo = Button(self.frame_menu, text = "Kirim Saldo",
                                         width = 15, height =8, command = self.to_transaksi )
        self.tombol_kirim_saldo.grid(row =1, column =1)

        #buat frame biodata
        self.frame_biodata = LabelFrame (self.master, height =270, width =170)
        self.frame_biodata.place (x= 300, y=150)


        #label user
        text1 = Label (self.frame_biodata, text = "INFO AKUN", font = ('consolas',
                                12, "bold"), fg = "blue4" )
        text1.grid (row =1 , column = 0)

    def to_daftar_agen (self) :
        self.to_daftar_agen = Toplevel(self.master)
        self.app=view_daftar_agen.daftar_agen(self.to_daftar_agen)

    def to_daftar_paket (self) :
        self.to_daftar_paket = Toplevel(self.master)
        self.app=view_daftar_paket.daftar_paket(self.to_daftar_paket)

    def info (self) :
       messagebox.showinfo("failed", "sistem dalam perbaikan")

    def to_transaksi (self) :
        self.to_transaksi = Toplevel(self.master)
        self.app=view_transfer.transaksi(self.to_transaksi)
'''
root = Tk()
obj=main_menu_admin(root)
root.mainloop()'''

