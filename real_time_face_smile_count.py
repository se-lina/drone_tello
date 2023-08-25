import cv2  
  
# カスケード分類器の読み込み  
face_cascade = cv2.CascadeClassifier('/Users/lina/Desktop/keio_pg_test/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')  
smile_cascade = cv2.CascadeClassifier('/Users/lina/Desktop/keio_pg_test/opencv-master/data/haarcascades/haarcascade_smile.xml')    

# カメラの起動  
cap = cv2.VideoCapture(0)  
  
while True:  
    # フレームの取得  
    ret, frame = cap.read()  
  
    # グレースケール変換  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
  
    # 顔の検出  
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)  
  
    # 顔の数をカウント  
    num_faces = len(faces)  
  
    # 顔を四角で囲む  
    for (x, y, w, h) in faces:  
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
        cv2.putText(frame, 'face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
  
        # Crop face region  
        roi_gray = gray[y:y+h, x:x+w]  
        roi_color = frame[y:y+h, x:x+w]  
  
        # Detect smiles in face region  
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)  
  
        # Draw rectangle around each smile  
        for (sx, sy, sw, sh) in smiles:  
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 255), 2)  
            cv2.putText(roi_color, 'smile', (sx, sy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2) 
  
        # Check if smiles were detected  
        if len(smiles) > 0:  
            # Add code to be executed when a smile is detected  
            print('笑顔見つけた！')  

    # 画像内に人の顔の数を表示  
    cv2.putText(frame, 'Number of faces: ' + str(num_faces), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)  
  
    # 画像の表示  
    cv2.imshow('frame', frame)  
  
    # 終了キーの取得  
    key = cv2.waitKey(1)  
  
    # 終了キーが押されたらループを抜ける  
    if key == 27:  
        break  
  
# カメラの停止  
cap.release()  
cv2.destroyAllWindows()  
