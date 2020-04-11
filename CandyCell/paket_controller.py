import redis

class Paket_controller :
    def __init__(self) :
        self.ccell = redis.Redis(
               host='127.0.0.1',
               port=6379, db=1)

    def get_indosat ():
        kode_produk = []
        details = []
        hargas = []
        paket_indosat = ('paket_1', 'paket_2', 'paket_3', 'paket_4',
                          'paket_5', 'paket_6', 'paket_7', 'paket_8'
                        'paket_9', 'paket_10')
        for i in paket_indosat :
            kode = ' '.join(map(str, (ccell.hmget(i, 'kode_produk'))))
            kode = kode.replace('b','')
            kode_produk.append(kode)
   
            detail = ' '.join(map(str, (ccell.hmget(i, 'detail'))))
            detail = detail.replace('b','')
            details.append(detail)
    
            harga = ' '.join(map(str, (ccell.hmget(i, 'harga'))))
            harga = harga.replace('b','')
            hargas.append(harga)
        return 
       '''
        print ("kode produk :", kode_produk)
        print ("detail :", details)
        print ("harga:", hargas)
        '''
    def get_xl ():
        kode_produk = []
        details = []
        hargas = []
        paket_XL = ('paket_11', 'paket_12', 'paket_13', 'paket_14',
                    'paket_15', 'paket_16', 'paket_17', 'paket_18'
                    'paket_19', 'paket_20')
        for i in paket_XL :
            kode = ' '.join(map(str, (ccell.hmget(i, 'kode_produk'))))
            kode = kode.replace('b','')
            kode_produk.append(kode)
       
            detail = ' '.join(map(str, (ccell.hmget(i, 'detail'))))
            detail = detail.replace('b','')
            details.append(detail)
        
            harga = ' '.join(map(str, (ccell.hmget(i, 'harga'))))
            harga = harga.replace('b','')
            hargas.append(harga)
        '''    
        print ("kode produk :", kode_produk)
        print ("detail :", details)
        print ("harga:", hargas)
        '''
    def get_telkomsel ():
        kode_produk = []
        details = []
        hargas = []
        paket_tsel = ('paket_21', 'paket_22', 'paket_23', 'paket_24',
                    'paket_25', 'paket_26', 'paket_27', 'paket_28'
                    'paket_29', 'paket_30')
        for i in paket_tsel :
            kode = ' '.join(map(str, (ccell.hmget(i, 'kode_produk'))))
            kode = kode.replace('b','')
            kode_produk.append(kode)
       
            detail = ' '.join(map(str, (ccell.hmget(i, 'detail'))))
            detail = detail.replace('b','')
            details.append(detail)
        
            harga = ' '.join(map(str, (ccell.hmget(i, 'harga'))))
            harga = harga.replace('b','')
            hargas.append(harga)
        '''    
        print ("kode produk :", kode_produk)
        print ("detail :", details)
        print ("harga:", hargas)
        '''
    def get_ovo ():
        kode_produk = []
        details = []
        hargas = []
        paket_ovo = ('paket_31', 'paket_32', 'paket_33', 'paket_34',
                    'paket_35', 'paket_36', 'paket_37', 'paket_38'
                    'paket_39', 'paket_40')
        for i in paket_ovo :
            kode = ' '.join(map(str, (ccell.hmget(i, 'kode_produk'))))
            kode = kode.replace('b','')
            kode_produk.append(kode)
       
            detail = ' '.join(map(str, (ccell.hmget(i, 'detail'))))
            detail = detail.replace('b','')
            details.append(detail)
        
            harga = ' '.join(map(str, (ccell.hmget(i, 'harga'))))
            harga = harga.replace('b','')
            hargas.append(harga)
        '''    
        print ("kode produk :", kode_produk)
        print ("detail :", details)
        print ("harga:", hargas)
        '''
    def get_dana ():
        kode_produk = []
        details = []
        hargas = []
        paket_dana = ('paket_41', 'paket_42', 'paket_43', 'paket_44',
                    'paket_45', 'paket_46', 'paket_47', 'paket_48'
                    'paket_49', 'paket_50')
        for i in paket_dana :
            kode = ' '.join(map(str, (ccell.hmget(i, 'kode_produk'))))
            kode = kode.replace('b','')
            kode_produk.append(kode)
       
            detail = ' '.join(map(str, (ccell.hmget(i, 'detail'))))
            detail = detail.replace('b','')
            details.append(detail)
        
            harga = ' '.join(map(str, (ccell.hmget(i, 'harga'))))
            harga = harga.replace('b','')
            hargas.append(harga)
        '''    
        print ("kode produk :", kode_produk)
        print ("detail :", details)
        print ("harga:", hargas)
        '''            
    def get_pln ():
        kode_produk = []
        details = []
        hargas = []
        paket_pln = ('paket_51', 'paket_52', 'paket_53', 'paket_54',
                    'paket_55', 'paket_56')
        for i in paket_pln :
            kode = ' '.join(map(str, (ccell.hmget(i, 'kode_produk'))))
            kode = kode.replace('b','')
            kode_produk.append(kode)
       
            detail = ' '.join(map(str, (ccell.hmget(i, 'detail'))))
            detail = detail.replace('b','')
            details.append(detail)
        
            harga = ' '.join(map(str, (ccell.hmget(i, 'harga'))))
            harga = harga.replace('b','')
            hargas.append(harga)
        '''    
        print ("kode produk :", kode_produk)
        print ("detail :", details)
        print ("harga:", hargas)
        '''
