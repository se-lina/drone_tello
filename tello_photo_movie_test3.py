import time
import cv2
from threading import Thread
from djitellopy import Tello

class TelloController:
    def __init__(self):
        # DJI Telloと接続
        self.tello = Tello()
        self.tello.connect()

        # 映像ストリームを開始
        self.keepRecording = True
        self.tello.streamon()
        self.frame_read = self.tello.get_frame_read()

        # 映像を録画するスレッドを作成
        self.recorder_thread = Thread(target=self.videoRecorder)
        self.recorder_thread.start()

        # Telloの操作を受け取るスレッドを作成
        self.run_thread = Thread(target=self.run)
        self.run_thread.start()

        # 初期化
        self.flying = False
        self.displayTelloStatus()

    def videoRecorder(self):
        # 現在時刻を取得
        current_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
        # 動画を保存するファイル名を作成
        filename = f'{current_time}.mp4'
        # 動画ファイルを作成
        height, width, _ = self.frame_read.frame.shape
        video = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

        while self.keepRecording:
            video.write(self.frame_read.frame)
            time.sleep(1 / 30)

        video.release()

    def run(self):
        # キーボード入力によるTelloの操作
        time.sleep(7)
        while self.keepRecording:
            # キー入力を待機
            key = input('操作キーの入力: ')

            # 離陸
            if self.flying == False and key == 't':
                self.tello.takeoff()
                self.flying = True

            # 着陸
            elif self.flying == True and key == 'l':
                self.tello.land()
                self.flying = False

            # 上昇
            elif self.flying == True and key == 'u':
                num = input('何cm上昇するか入力(20~500): ')
                if num.isdecimal() and 20 <= int(num) <= 500:
                    self.tello.move_up(int(num))

            # 下降
            elif self.flying == True and key == 'j':
                num = input('何cm下降するか入力(20~500): ')
                if num.isdecimal() and 20 <= int(num) <= 500:
                    self.tello.move_down(int(num))
            
            # 前進
            elif self.flying == True and key == 'w':
                num = input('何cm前進するか入力(20~500): ')
                if num.isdecimal() and 20 <= int(num) <= 500:
                    self.tello.move_forward(int(num))
        
            # 後進
            elif self.flying == True and key == 's':
                num = input('何cm後進するか入力(20~500): ')
                if num.isdecimal() and 20 <= int(num) <= 500:
                    self.tello.move_back(int(num))

            # 右進
            elif self.flying == True and key == 'd':
                num = input('何cm右に進むか入力(20~500): ')
                if num.isdecimal() and 20 <= int(num) <= 500:
                    self.tello.move_right(int(num))

            # 左進
            elif self.flying == True and key == 'a':
                num = input('何cm左に進むか入力(20~500): ')
                if num.isdecimal() and 20 <= int(num) <= 500:
                    self.tello.move_left(int(num))

            # 回転
            elif self.flying == True and key == 'r':
                num = input('何度回転するか入力(1~360): ')
                if num.isdecimal() and 1 <= int(num) <= 360:
                    self.tello.rotate_clockwise(int(num))

            # 写真撮影(タイマーの設定)
            elif key == 'p':
                num = input('待ち時間の入力(0~10): ')
                if num.isdecimal() and 0 <= int(num) <= 10:
                    time.sleep(int(num))
                    current_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
                    pic_name = f'{current_time}.jpg'
                    cv2.imwrite(pic_name, self.frame_read.frame)

            # 終了
            elif self.flying == False and key == 'q':
                cv2.destroyWindow('Tello')
                self.keepRecording = False
                break
            
    def displayTelloStatus(self):
        # リアルタイム映像の表示
        while self.keepRecording:
            # 画面上部に表示する情報の設定
            battery = self.tello.get_battery()
            flight_time = self.tello.get_flight_time()
            height = self.tello.get_height()
            display_text = f'Battery: {battery}%  Flight Time: {flight_time}s  Height: {height}cm'
            cv2.putText(self.frame_read.frame, display_text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

            # 映像の表示
            cv2.imshow('display', self.frame_read.frame)

            # qキーで終了
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyWindow('display')
                self.keepRecording = False
                break

        # スレッドを停止
        self.recorder_thread.join()
        self.run_thread.join()
        self.tello.end()

TelloController()
