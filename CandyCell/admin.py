import redis

class Admin  :
    def __init__(self) :
        self.ccell = redis.Redis(
               host='127.0.0.1',
               port=6379, db=1)

    def getAdmin (self, key=None) :
        return self.ccell.hgetall(key)

    def getValue (self, key, field) :
        return self.ccell.hmget(key, field)
    
    def add (self, key, kode_produk, detail, harga):
        dict_paket = {'nama': nama, 'username': username, 'password': password}
        return self.ccell.hmset (key, dict)

admin= Admin()
