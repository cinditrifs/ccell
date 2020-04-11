from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import redis
import connect

ccell = redis.Redis(
           host='127.0.0.1',
           port=6379, db='1')

class daftar_agen :
    def __init__(self, root) : 
        self.master = root
        self.master.title("DAFTAR AGEN")
        self.master.geometry("500x500+350+120")
        self.master.config(bg="lightskyblue2")

        self.title_1=Label(self.master, text="CANDYSELL", font=(
                        "times new roman", 10, "bold"), bg="deepskyblue3",
                         fg="white", bd=10)     
        self.title_1.place(x=2, y=1)

        self.title_2 = Label(self.master, text = "DAFTAR AGEN",
                            font = ("Times new roman", 15, 'bold'), bg = "white",
                            fg = "deepskyblue3")
        self.title_2.place(x= 0, y= 50, relwidth = 1)
    
        #buat frame naro daftar agen
        self.frame = LabelFrame(self.master)
        self.frame.place (x= 60, y = 160)
          
        keys = ('agen_001', 'agen_002', 'agen_003', 'agen_004', 'agen_005', 'agen_006',
               'agen_007', 'agen_008', 'agen_009', 'agen_010')
        namas = []
        id_agen = []
        no_tlp =[]
        for i in keys :
            name = ccell.hmget(i, 'name')
            namas.append(name)
            idAgen = ccell.hmget(i, 'id_agen')
            id_agen.append(idAgen)
            tlp = ccell.hmget(i, 'tlp_num')
            no_tlp.append(tlp)
            
        #print(namas)
        #print(type(name))

        #list box name
        listbox1 = Listbox(self.frame, height=15, bg= "white")
        listbox1.grid(column=0, row=0)
        for nama in range(len(namas)) :
            listbox1.insert (nama, namas[nama])
               
        #list box id
        listbox2 = Listbox(self.frame, height=15, bg= "white")
        listbox2.grid(column=1, row=0)
        for idAgen in range(len(id_agen)) :
            listbox2.insert (idAgen, id_agen[idAgen])

        #list box tlp number
        listbox3 = Listbox(self.frame, height=15, bg= "white")
        listbox3.grid(column=2, row=0)
        for tlp in range(len(no_tlp)) :
            listbox3.insert (tlp, no_tlp[tlp])

        #buat label Nama, Id_agen, nomor tlp
        self.frame_ket = LabelFrame(self.master, width = 100)
        self.frame_ket.place (x= 60, y = 140)
        
        namaTxt =Label(self.frame_ket, text = "Nama")
        idTxt =Label(self.frame_ket, text = "Id Agen")
        tlpTxt =Label(self.frame_ket, text = "Nomor Telp")

        namaTxt.grid(column = 0, row=0, padx= 40 )
        idTxt.grid(column = 1, row=0, padx= 40)
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
print (ccell.hmget('admin_001', 'password'))   
