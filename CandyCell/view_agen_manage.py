from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import redis
import connect
import view_transaksi

ccell = redis.Redis(
           host='127.0.0.1',
           port=6379, db='1')

def mulai():
    root = Tk()
    app = main_menu_agen(root)

class main_menu_agen :
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
        self.tombol_transaksi = Button(self.frame_menu, text = "Transaksi",
                                         width = 15, height =8,
                                       command = self.to_transaksi)
        self.tombol_transaksi.grid(row =0, column =0)
        
        self.tombol_daftar_harga = Button(self.frame_menu, text = "Daftar Harga",
                                         width = 15, height =8,
                                          command = self.to_daftar_paket)
        self.tombol_daftar_harga.grid(row =0, column =1)

        self.tombol_riwayat_transaksi = Button(self.frame_menu, text = "Riwayat Transaksi",
                                         width = 15, height =8,
                                               command = self.info)
        self.tombol_riwayat_transaksi.grid(row =1, column =0)

        self.tombol_minta_saldo = Button(self.frame_menu, text = "Minta Saldo",
                                         width = 15, height =8)
        self.tombol_minta_saldo.grid(row =1, column =1)

        #buat frame biodata
        self.frame_biodata = LabelFrame (self.master, height =270, width =170)
        self.frame_biodata.place (x= 300, y=150)

        #label user
        text1 = Label (self.frame_biodata, text = "INFO AKUN", font = ('consolas',
                                12, "bold"), fg = "blue4" )
        text1.grid (row =1 , column = 0)

    def to_daftar_paket (self) :
        self.to_daftar_paket = Toplevel(self.master)
        self.app=daftar_paket(self.to_daftar_paket)

    def to_transaksi (self) :
        self.to_transaksi = Toplevel(self.master)
        self.app=view_transaksi.transaksi(self.to_transaksi)

    def info (self) :
       messagebox.showinfo("failed", "sistem dalam perbaikan")
        


class daftar_paket :
    def __init__(self, root) : 
        self.master = root
        self.master.title("DAFTAR PAKET")
        self.master.geometry("500x500+350+120")
        self.master.config(bg="lightskyblue2")

        self.title_1=Label(self.master, text="CANDYSELL", font=(
                        "times new roman", 10, "bold"), bg="deepskyblue3",
                         fg="white", bd=10)     
        self.title_1.place(x=2, y=1)

        self.title_2 = Label(self.master, text = "DAFTAR PAKET",
                            font = ("Times new roman", 15, 'bold'), bg = "white",
                            fg = "deepskyblue3")
        self.title_2.place(x= 0, y= 50, relwidth = 1)

        #buat frame naro daftar agen
        self.frame = LabelFrame(self.master)
        self.frame.place (x= 20, y = 160)
          
        keys = ('paket_1', 'paket_2', 'paket_3', 'paket_4',
                'paket_5', 'paket_6', 'paket_7', 'paket_8', 
                'paket_9', 'paket_10', 'paket_11', 'paket_12',
                'paket_13', 'paket_14', 'paket_15', 'paket_16',
                'paket_17', 'paket_18' , 'paket_19', 'paket_20',
                'paket_21', 'paket_22', 'paket_23', 'paket_24',
                'paket_25', 'paket_26', 'paket_27', 'paket_28',
                'paket_29', 'paket_30', 'paket_31', 'paket_32',
                'paket_33', 'paket_34', 'paket_35', 'paket_36',
                'paket_37', 'paket_38', 'paket_39', 'paket_40',
                'paket_41', 'paket_42', 'paket_43', 'paket_44',
                'paket_45', 'paket_46', 'paket_47', 'paket_48' ,
                'paket_49', 'paket_50', 'paket_51', 'paket_52',
                'paket_53', 'paket_54',
                'paket_55', 'paket_56')
        kode_product = []
        details = []
        prices = []
        for i in keys :
            kode = ccell.hmget(i, 'kode_produk')
            kode_product.append(kode)
            detail = ccell.hmget(i, 'detail')
            details.append(detail)
            harga = ccell.hmget(i, 'harga')
            prices.append(harga)
            
        #print(namas)
        #print(type(name))

        #list box name
        listbox1 = Listbox(self.frame, height=20, width = 15 ,bg= "white")
        listbox1.grid(column=0, row=0)
        for kode in range(len(kode_product)) :
            listbox1.insert (kode, kode_product[kode])
               
        #list box id
        listbox2 = Listbox(self.frame, height= 20, width = 45 ,bg= "white")
        listbox2.grid(column=1, row=0)
        for detail in range(len(details)) :
            listbox2.insert (detail, details[detail])

        #list box tlp number
        listbox3 = Listbox(self.frame, height=20, width= 15, bg= "white")
        listbox3.grid(column=2, row=0)
        for harga in range(len(prices)) :
            listbox3.insert (harga, prices[harga])

        #buat label Nama, Id_agen, nomor tlp
        self.frame_ket = LabelFrame(self.master, width = 100)
        self.frame_ket.place (x= 20, y = 138)
        
        namaTxt =Label(self.frame_ket, text = "Kode Paket")
        idTxt =Label(self.frame_ket, text = "Detail")
        tlpTxt =Label(self.frame_ket, text = "Harga")

        namaTxt.grid(column = 0, row=0, padx= 10 )
        idTxt.grid(column = 1, row=0, padx= 120)
        tlpTxt.grid(column = 2, row=0, padx= 30)
        
if __name__ == '__main__':
    mulai()

