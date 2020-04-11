import redis
from admin import Admin

class Admin_controller :
    def __init__ (self) :
        self.admin_controller = Admin ()
        self.ccell = redis.Redis(
               host='127.0.0.1',
               port=6379, db=1)

    def get_all_admin (self, keys) :
        keys = ('admin_001', 'admin_002', 'admin_003')
        for key in keys :
            print( admin.self.ccell.hgetall(key))

    def get_admin (self) :
        pass

    def get_password (self):
        return admin.Admin.getValue(password)

AdminController = Admin_controller()

#print(AdminController.get_all_admin)

