# 実行前にダウンロード
# https://github.com/opencv/opencv/tree/master/data/haarcascades

import cv2  
  
# カスケード分類器の読み込み  
face_cascade = cv2.CascadeClassifier('/Users/lina/Desktop/keio_pg_test/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')  
  
# ビデオファイルの読み込み  
cap = cv2.VideoCapture('/Users/lina/Desktop/keio_pg_test/video.mp4')  
  
# ビデオファイルが正常に読み込まれた場合  
if cap.isOpened():  
  
    # フレームを1枚ずつ取得して処理する  
    while True:  
        ret, frame = cap.read()  
  
        # フレームの取得に失敗した場合はループを抜ける  
        if not ret:  
            break  
  
        # グレースケールに変換  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
  
        # 顔検出  
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  
  
        # 検出された顔に矩形を描画する  
        for (x, y, w, h) in faces:  
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  
  
        # 結果の表示  
        cv2.imshow("Video", frame)  
  
        # 'q'キーが押されたら終了する  
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break  
  
# 後処理  
cap.release()  
cv2.destroyAllWindows()  
