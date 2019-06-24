# -*- coding: utf-8 -*-
from redis import StrictRedis


redis = StrictRedis(host='192.168.138.191',
                    port='6380',
                    db=0)

redis.set('test1', 'aaa')

ret = redis.get('test1')

print(ret)
