# 実行前にダウンロード
# https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2  
  
# 画像の読み込み  
# ファイルのパスを入力するときに注意が必要です。
image = cv2.imread('/Users/lina/Desktop/keio_pg_test/model.jpg')  
  
# グレースケールに変換  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
  
# 顔検出用の分類器の読み込み  
# ファイルのパスを入力するときに注意が必要です。
cascade_path = '/Users/lina/Desktop/keio_pg_test/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml'  
cascade = cv2.CascadeClassifier(cascade_path)  
  
# 顔検出の実行  
faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))  
  
# 検出された顔を矩形で囲む  
for (x, y, w, h) in faces:  
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)  
  
# 結果の表示  
cv2.imshow('image', image)  
  
# キーボードからの入力を待つ 
# 終了させる場合、qキーを押します。 
while True:  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
# ウィンドウを閉じる  
cv2.destroyAllWindows()  
