import redis

class Paket  :
    def __init__(self) :
        self.ccell = redis.Redis(
               host='127.0.0.1',
               port=6379, db=1)

    def getPaket (self, key=None) :
        return self.ccell.hgetall(key)

    def getValue (self, key, field) :
        return self.ccell.hmget(key, field)
    
    def add (self, key, kode_produk, detail, harga):
        dict_paket = {'kode_produk': kode_produk, 'detail': detail, 'harga': harga}
        return self.ccell.hmset (key, dict)

    
paket= Paket()

#print(paket.getPaket('paket_1'))
#print(paket.getPaket('paket_2'))
