# Tello Python3 Control Basic 
# http://www.ryzerobotics.com/
# https://blog.hatena.ne.jp/se-lina/
#
# 12 Feb 2023


import socket
import time

#Create a UDP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1' , 8889)

#command-mode : 'command'
#ドローンを起動させます
socket.sendto('command'.encode('utf-8'),tello_address)
print ('start')

#離陸させます
socket.sendto('takeoff'.encode('utf-8'),tello_address)
print ('takeoff')

time.sleep(5) #5秒待ちます

#ドローンに動きを指示します
#1ｍ上昇する
socket.sendto('up 100'.encode('utf-8'),tello_address)
time.sleep(5) #5秒待ちます
#1ｍ前進する
socket.sendto('forward 100'.encode('utf-8'),tello_address)
time.sleep(5) #5秒待ちます
#1ｍ左に動く
socket.sendto('left 100'.encode('utf-8'),tello_address)
time.sleep(5) #5秒待ちます
#1ｍ後進する
socket.sendto('back 100'.encode('utf-8'),tello_address)
time.sleep(5) #5秒待ちます
#1ｍ右に動く
socket.sendto('right 100'.encode('utf-8'),tello_address)
time.sleep(5) #5秒待ちます

#着陸させます
socket.sendto('land'.encode('utf-8'),tello_address)
print ('land')
