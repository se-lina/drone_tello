import time
import cv2
from threading import Thread
from djitellopy import Tello
  
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
class TelloController:
    def __init__(self):
        # Telloとの接続
        self.tello = Tello()
        self.tello.connect()

        # 変数の定義
        self.recording = True
        self.flying = False
        self.timer = 0
        self.count = 0

        # 映像ストリームを開始
        self.tello.streamon()
        self.frame_read = self.tello.get_frame_read()

        # 各スレッドの作成
        self.recorder_thread = Thread(target=self.recorder)
        self.recorder_thread.start()

        self.run_thread = Thread(target=self.run)
        self.run_thread.start()

        self.keeping_thread = Thread(target=self.keeping)
        self.keeping_thread.start()

        # 関数の呼び出し
        self.displayTelloStatus()

    def recorder(self):
        # 動画ファイル名の作成
        current_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
        filename = f'{current_time}.mp4'

        # 動画ファイルの作成
        height, width, _ = self.frame_read.frame.shape
        video = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

        while self.recording:
            video.write(self.frame_read.frame)
            time.sleep(1 / 30)

        video.release()

    def run(self):
        while self.recording:
            battery = self.tello.get_battery()

            # 停止中の処理
            if self.flying == False:
                key = input('離陸(Tキー)・終了(Qキー)・航路番号を選択: ')

                # 離陸
                if key == 't' and battery > 10:
                    self.timer = time.time()
                    self.flying = True
                    self.tello.takeoff()
                
                elif key == 't' and battery <= 10:
                    print('充電が足りません')
                
                # 航路1
                elif key == '1':
                    self.tello.takeoff()
                    self.tello.rotate_clockwise(360)
                    self.tello.land()

                # self.flyingを手動で切り替え
                elif key == 'flying':
                    self.flying = True

                # 終了
                elif key == 'q':
                    self.recording = False
                    cv2.destroyAllWindows()
                    break
            
            # 飛行中の処理
            elif self.flying == True:
                key = input('操作キーの入力: ')

                # 着陸
                if key == 'l':
                    self.flying = False
                    self.tello.land()
                    time.sleep(3)

                # 上昇
                elif key == 'u':
                    num = input('何cm上昇しますか(20~500): ')
                    if num.isdecimal() and 20 <= int(num) <= 500:
                        self.tello.move_up(int(num))

                # 下降
                elif key == 'j':
                    num = input('何cm下降しますか(20~500): ')
                    if num.isdecimal() and 20 <= int(num) <= 500:
                        self.tello.move_down(int(num))
            
                # 前進
                elif key == 'w':
                    num = input('何cm前進しますか(20~500): ')
                    if num.isdecimal() and 20 <= int(num) <= 500:
                        self.tello.move_forward(int(num))
        
                # 後進
                elif key == 's':
                    num = input('何cm後進しますか(20~500): ')
                    if num.isdecimal() and 20 <= int(num) <= 500:
                        self.tello.move_back(int(num))

                # 右進
                elif key == 'd':
                    num = input('何cm右に進みますか(20~500): ')
                    if num.isdecimal() and 20 <= int(num) <= 500:
                        self.tello.move_right(int(num))

                # 左進
                elif key == 'a':
                    num = input('何cm左に進みますか(20~500): ')
                    if num.isdecimal() and 20 <= int(num) <= 500:
                        self.tello.move_left(int(num))

                # 時計回り
                elif key == 'r':
                    num = input('何度時計回りしますか(1~360): ')
                    if num.isdecimal() and 1 <= int(num) <= 360:
                        self.tello.rotate_clockwise(int(num))

                # 反時計回り
                elif key == 'f':
                    num = input('何度反時計回りしますか(1~360): ')
                    if num.isdecimal() and 1 <= int(num) <= 360:
                        self.tello.rotate_counter_clockwise(int(num))
            
                # 速度の指定
                elif key == 'speed':
                    num = input('速度cm/sを入力(10~100): ')
                    if num.isdecimal() and 1 <= int(num) <= 100:
                        self.tello.set_speed(int(num))

                # 写真撮影
                elif key == 'p':
                    num = input('何秒後に撮影しますか(0~10): ')
                    if num.isdecimal() and 0 <= int(num) <= 10:
                        time.sleep(int(num))
                        # JPG形式で画像を出力
                        current_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
                        pic_name = f'{current_time}.jpg'
                        cv2.imwrite(pic_name, self.frame_read.frame)

                # self.flyingを手動で切り替え
                elif key == 'flying':
                    self.flying = False

                # エラー検証用
                elif key == 'error':
                    self.tello.takeoff()
    
    def keeping(self):
        while self.recording:
            if self.flying:
                if time.time() - self.timer >= 15:
                    self.tello.send_command_without_return('command')
                
                    # timer・countの更新
                    self.timer = time.time()
                    self.count += 1
                    print('Enterキーを押してください')

    def displayTelloStatus(self):
        # 説明画像の表示
        # 画像のパスを見るときに注意
        sheet = cv2.imread('/Users/lina/Desktop/keio_pg_test/instruct.jpg', cv2.IMREAD_UNCHANGED)
        cv2.imshow('cheat sheet', sheet)
        cv2.moveWindow('cheat sheet', 500, 0)

        while self.recording:
            # 画面上部に表示する情報の設定
            battery = self.tello.get_battery()
            flight_time = self.tello.get_flight_time()
            height = self.tello.get_height()
            display_text = f'Battery: {battery}%  Flight Time: {flight_time}s  Height: {height}cm'
            cv2.putText(self.frame_read.frame, display_text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                        (0, 255, 0), 1, cv2.LINE_AA)

            # 映像の表示
            cv2.imshow('Tello camera', self.frame_read.frame)

            # 終了
            if cv2.waitKey(1) & 0xFF == ord('q') and self.flying == False:
                self.recording = False
                cv2.destroyAllWindows()
                break

        # スレッドを停止
        self.recorder_thread.join()
        self.run_thread.join()
        self.keeping_thread.join()
        self.tello.end()

TelloController()

# Telloのカメラを停止  
tello.streamoff()  
  
# Telloとの接続を切断  
tello.end()  
  
# ウィンドウを解放  
cv2.destroyAllWindows()  
