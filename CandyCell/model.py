import redis
import json

ccell = redis.Redis(
           host='127.0.0.1',
           port=6379, db=1)

def get_value (key, field):
    return ccell.hmget(key, field)
'''
print(get_value('admin_001', 'username')
j
      jjj= ccell.hmget('admin_001', 'username')
print (op)

opp= ccell.hscan('admin_002')
print(opp)

opop= ccell.hgetall('admin_001')
print(opop)
'''
keys = ccell.keys()
for key in keys :
      print (key)
      
      
       

