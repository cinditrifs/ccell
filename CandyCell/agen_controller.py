import redis
from agen import Agen

class Agen_controller :
    def __init__ (self) :
        self.agen_controller = Agen ()
        self.ccell = redis.Redis(
               host='127.0.0.1',
               port=6379, db=1)

    def get_all_agen (self, keys) :
        keys = ('agen_001', 'agen_002', 'agen_003', 'agen_004', 'agen_005', 'agen_006',
               'agen_007', 'agen_008', 'agen_009', 'agen_010')
        for key in keys :
            return admin.self.ccell.hgetall(key)

    def get_admin (self) :
        pass

    def get_pin (self):
        return admin.Admin.getValue(pin)

AgenController = Agen_controller()


#print(AgenController.get_all_agen)
