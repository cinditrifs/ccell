import redis

class Agen  :
    def __init__(self) :
        self.ccell = redis.Redis(
               host='127.0.0.1',
               port=6379, db=1)

    def getAgen (self, key=None) :
        return self.ccell.hgetall(key)

    def getValue (self, key, field) :
        return self.ccell.hmget(key, field)
    
    def add (self, key, name, id_agen, tlp_num, pin):
        dict_paket = {'nama': nama, 'id_agen' : id_agen, 'tlp_num' :tlp_num, 'pin' : pin}
        return self.ccell.hmset (key, dict)

agen= Agen()
