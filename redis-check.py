#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
用于检测全网redis服务器是否可以远程无密码登陆，以便提醒管理员加固，避免被挖矿病毒利用。
'''


import socket
import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库


# host_list = ['ali2.teeh.cn']

host_list = []
for ip in range(1,255):
    host_list.append('10.10.4.'+str(ip))
tgtPort = '6379'
ok_redis = dict()
bad_redis = dict()


for tgtHost in host_list:
    is_redis = ""

    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(2)
        sk.connect((tgtHost,int(tgtPort)))
        sk.close()
    except socket.timeout:
        print(tgtHost,"not redis.")
    except ConnectionRefusedError:
        print(tgtHost, "not redis.")
    else:
        print(tgtHost,"is redis.")
        is_redis = 1


    # 检测redis是否可以远程无密码登陆
    if is_redis:
        r = redis.Redis(host=tgtHost, port=tgtPort,
                        decode_responses=True)  # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
        try:
            response = r.client_list()
        except redis.exceptions.ResponseError:
            print("Need Auth")
            ok_redis[tgtHost] = "need Auth"
        else:
            print('Bad')
            bad_redis[tgtHost] = "Bad"

print("Redis service is ok:")
for k,v in ok_redis.items():
    print(k,v)

print('\nRedis service is BAD:')
for k,v in bad_redis.items():
    print(k,v)








