from djitellopy import Tello  
import cv2  
  
# Telloに接続  
tello = Tello()  
tello.connect()  
  
# Telloのカメラを開始  
tello.streamon()  
  
# Haar Cascadeファイルを読み込み  
face_cascade = cv2.CascadeClassifier('/Users/lina/Desktop/keio_pg_test/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')  
  
while True:  
    # Telloのカメラからフレームを取得  
    frame = tello.get_frame_read().frame  
  
    # グレースケールに変換  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
  
    # 顔検出を実行  
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)  
  
    # 検出された顔に矩形を描画  
    for (x, y, w, h) in faces:  
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
        cv2.putText(frame, 'face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)  
  
    # 結果を表示  
    cv2.imshow('frame', frame)  
  
    # 'q'キーを押すとループを抜ける  
    if cv2.waitKey(1) == ord('q'):  
        break  
  
# Telloのカメラを停止  
tello.streamoff()  
  
# Telloとの接続を切断  
tello.end()  
  
# ウィンドウを解放  
cv2.destroyAllWindows()  
