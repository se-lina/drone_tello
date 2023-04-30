# 小型ドローンTelloを活用した操作方法と画像取得、OpenCVを活用した例(未完成・製作中)

## 概要
ここでは、小型ドローンTelloを使用した動作プログラミングをまとめ  
OpenCVライブラリを使用した、画像の処理を行うプログラミングをまとめます。
- 基本的なTelloの操作、起動方法 (4/17)
- Telloから画像・動画を取得する方法 (5/1)
- その画像から物体を検出する方法 (5/1)
- それらの準備（pip installなど） (5/1)
- ChatGPTを活用した例など

## 基本的なTelloの操作、起動方法
小型ドローンTelloの動作プログラミングをここにまとめます。  
各自のパソコンでここに記載のPythonコードでドローンを動かすことが出来ます。  
通信方式はUDP（パソコンとTelloｏをＷｉｆｉでつなぐ）です。  
そのため、WiFiでの接続時はインターネットできません。  
  
TelloのSDKを使いPythonコードでドローンを動かします。  
SDKの詳細は以下からダウンロードしてください。  
 
### SDK
日本語（Selina翻訳）  
https://drive.google.com/file/d/1A51f-5HK5fq4YfiIR4Anun4DD8ERRtR3/view?usp=sharing


#### 本家SDKのダウンロード先
＜SDK1.3＞  
https://www.ryzerobotics.com/jp/tello/downloads  
＜SDK2.0＞  
 https://www.ryzerobotics.com/jp/tello-edu/downloads. 
 
#### BLOG
やり方ブログ    
https://se-lina.hatenablog.com/entry/2020/08/16/110723
 
 
## 関連リンク
#### コードの詳細説明
https://github.com/se-lina/drone_tello/blob/main/details_description.md
#### 講義で必要なインストールモジュール
https://github.com/se-lina/drone_tello/blob/main/install_module.md


## Pythonプログラムコード例
#### Telloを動かすコード
https://github.com/se-lina/drone_tello/blob/main/tello_demo.py  
https://github.com/se-lina/drone_tello/blob/main/tello_demo2.py

#### Telloから動画、静止画を取得するコード
https://github.com/se-lina/drone_tello/blob/main/tello_photo_movie_test3.py

#### 静止画から顔を検出するコード
https://github.com/se-lina/drone_tello/blob/main/open_cv_face.py

#### 動画から顔を検出するコード
https://github.com/se-lina/drone_tello/blob/main/open_cv_face_douga.py
