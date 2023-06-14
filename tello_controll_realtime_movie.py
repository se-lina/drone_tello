import cv2  
import numpy as np  
import time  
import socket  
  
# Telloドローンとの通信を行うUDPソケットを作成  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
sock.bind(('', 9000))  
sock.sendto(b'command', ('192.168.10.1', 8889))  
sock.sendto(b'streamon', ('192.168.10.1', 8889))  
time.sleep(1)  
  
# Telloドローンから映像を取得  
stream_address = 'udp://0.0.0.0:11111'  
  
cap = cv2.VideoCapture(stream_address)  
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)  
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)  
  
# Telloドローンの制御を行うためのコード  
sock.sendto(b'takeoff', ('192.168.10.1', 8889))  
time.sleep(5)  
sock.sendto(b'forward 10', ('192.168.10.1', 8889))  
sock.sendto(b'left 10', ('192.168.10.1', 8889))  
sock.sendto(b'back 10', ('192.168.10.1', 8889))  
sock.sendto(b'right 10', ('192.168.10.1', 8889))  
sock.sendto(b'land', ('192.168.10.1', 8889))  
  
# 映像を表示  
while True:  
    ret, frame = cap.read()  
    if ret:  
        cv2.imshow('Tello Stream', frame)  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
# Telloドローンとの通信を終了  
sock.sendto(b'streamoff', ('192.168.10.1', 8889))  
sock.close()  
  
# OpenCVウィンドウを破棄  
cv2.destroyAllWindows()  
