# 実行前にダウンロード
# https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2  
  
# カスケード分類器の読み込み  
cascade_path = '/Users/lina/Desktop/keio_pg_test/opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml'  
cascade = cv2.CascadeClassifier(cascade_path)  
  
# 画像の読み込み  
img = cv2.imread('/Users/lina/Desktop/keio_pg_test/people.jpg')  
  
# グレースケール変換  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
# 顔検出  
faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))  
  
# 検出された顔に枠を描画  
count = len(faces)  
for (x, y, w, h) in faces:  
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  
  
# 人数を画像内に描画  
font = cv2.FONT_HERSHEY_SIMPLEX  
cv2.putText(img, 'Number of people: '+str(count), (50, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)  
  
# 結果表示  
cv2.imshow('result', img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
