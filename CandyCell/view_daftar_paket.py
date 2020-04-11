from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import redis

ccell = redis.Redis(
           host='127.0.0.1',
           port=6379, db='1')
'''
def mulai():
    root = Tk()
    app = daftar_paket(root)
'''   
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
        
        #buat button tambah, edit, hapus
        addButton = Button(self.master, text = 'tambah', width = 10,
                           command= self.info)
        editButton = Button(self.master, text = 'edit', width =10,
                            command= self.info)
        hapusButton = Button(self.master, text = 'hapus', width =10,
                             command= self.info)
        addButton.place(x= 70, y= 100)
        editButton.place(x= 200, y= 100)
        hapusButton.place(x= 340, y= 100)

    def info (self) :
       messagebox.showinfo("failed", "sistem dalam perbaikan")
        
        
        
                      
'''    
if __name__ == '__main__':
    mulai()'''

    
