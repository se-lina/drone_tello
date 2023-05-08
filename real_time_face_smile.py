import cv2  
  
# カメラからの入力を開始  
cap = cv2.VideoCapture(0)  

# Initialize face detector and smile detector  
face_cascade = cv2.CascadeClassifier('/Users/lina/Desktop/keio_pg_test/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')  
smile_cascade = cv2.CascadeClassifier('/Users/lina/Desktop/keio_pg_test/opencv-master/data/haarcascades/haarcascade_smile.xml')  
  
# Start video stream  
cap = cv2.VideoCapture(0)  
  
while True:  
    # Read frame from video stream  
    ret, frame = cap.read()  
  
    # Convert frame to grayscale  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
  
    # Detect faces in frame  
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  
  
    # Draw rectangle around each face  
    for (x, y, w, h) in faces:  
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  
        cv2.putText(frame, 'face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2) 
  
        # Crop face region  
        roi_gray = gray[y:y+h, x:x+w]  
        roi_color = frame[y:y+h, x:x+w]  
  
        # Detect smiles in face region  
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)  
  
        # Draw rectangle around each smile  
        for (sx, sy, sw, sh) in smiles:  
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)  
            cv2.putText(roi_color, 'smile', (sx, sy-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2) 
  
        # Check if smiles were detected  
        if len(smiles) > 0:  
            # Add code to be executed when a smile is detected  
            print('笑顔見つけた！')  
  
    # Display frame  
    cv2.imshow('Real-time face detection', frame)  
    cv2.waitKey(1)  
  
    # Exit loop on 'q' key press  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  

  
# Release video stream and close window  
cap.release()  
cv2.destroyAllWindows()  
