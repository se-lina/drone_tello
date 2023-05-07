# 小型ドローンTelloを活用した操作方法と画像取得、OpenCVを活用した例。リアルタイム物体検出。
2023/5/8時点：作成途中です。

## 目的
小型ドローンをPythonコードで動かし、指示通りの動作を学ぶことが出来る。  
TelloやPCのカメラを利用し、物体検出を学ぶことが出来る。  
これらを応用し、ドローンの動作と物体検出を同時に行い、社会活動で役に立てられるプログラム生成を習得することができる。  
プログラムを1から作り込むのではなく、すでにあるプログラムやライブラリを活用して、以下に早く目的を達成するかが、今回の目的です。

## 概要
ここでは、小型ドローンTelloを使用した動作プログラミングをまとめ  
OpenCVライブラリを使用した、画像の処理を行うプログラミングをまとめます。
- 基本的なTelloの操作、起動方法 (4/17)
- Telloから画像・動画を取得する方法 (5/1)
- 画像から物体を検出する方法 (5/1,8)
- 動画から物体を検出する方法 (5/1,8)
- それらの準備（pip installなど） (5/1,8)
- ChatGPTを活用した例など(5/1, 8)
- YOLOについて、引き継ぎの紹介など(5/8)
- 次回、Telloの編隊飛行（スウォーム）について

## 基本的なTelloの操作、起動方法
小型ドローンTelloの動作プログラミングをここにまとめます。  
各自のパソコンでここに記載のPythonコードでドローンを動かすことが出来ます。  
通信方式はUDP（パソコンとTelloをWiFiでつなぐ）です。  
そのため、WiFiでの接続時はインターネットできません。  

UDPについてはこちら  
https://wa3.i-3-i.info/word110.html
  
TelloのSDKを使いPythonコードでドローンを動かします。  
SDKの詳細は以下からダウンロードしてください。  
 
### SDK
日本語（Lina　Katayose翻訳）  
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
※ここにコードの説明などをまとめて書いていきます。筆者のメモとしても使います。

#### 講義で必要なインストールモジュール
https://github.com/se-lina/drone_tello/blob/main/install_module.md  
※OpenCVを利用する場合は、この事前準備が必要なので、このMarkDownファイルを事前に確認してください。

## Pythonプログラムコード例
※筆者はMac OSで書いているため、一部ディレクトリ構造などはWindows, Linuxと異なる場合がありますので適宜修正し、実行してください。

### (基礎編 1)Telloの基本的な動作プログラム

#### Telloを動かすコード
https://github.com/se-lina/drone_tello/blob/main/tello_demo.py  
https://github.com/se-lina/drone_tello/blob/main/tello_demo2.py

#### Telloから動画、静止画を取得するコード
▼事前準備が必要です。  
https://github.com/se-lina/drone_tello/blob/main/tello_controll.py  
(yasuta 作成サポート、5/8最新版)  
作成したプログラムには以下の機能があります。  
・プログラムの実行から終了までの動画をmp4形式で保存  
・キー入力で操作(離陸・着陸・前進・上昇等、お好みで増やせる)  
・Pキーを押すと写真を撮影し、jpgで保存  
・PC上にTelloのカメラ映像を表示(バッテリー残量・高度等の情報も表示)  
操作方法一覧は以下の画像でも確認出来ます。  
https://github.com/se-lina/drone_tello/blob/main/instruct.jpg


### (基礎編 2)Open CVを活用したオブジェクト検出のプログラム

#### 静止画から顔を検出するコード
▼事前準備が必要です。  
https://github.com/se-lina/drone_tello/blob/main/open_cv_face.py  
実行し、画像にある顔が検出されると四角で囲います。  
ループに入ってしまったとき 'q' キーでプログラムを終了できます。

#### 動画から顔を検出するコード
▼事前準備が必要です。  
https://github.com/se-lina/drone_tello/blob/main/open_cv_face_douga.py  
実行し、動画にある顔が検出されると四角で囲います。  
ループに入ってしまったとき 'q' キーでプログラムを終了できます。

### (応用編)

#### Open CVとTelloの動作プログラムを合わせたプログラム
https://github.com/se-lina/drone_tello/blob/main/open_cv_face_douga.py  
※プログラム実行中はキーボードの操作や動かす量の指示が必要なプログラムです。

#### リアルタイム顔検出
基礎編ではファイルを読み込んで顔検出をしたが、
ここではリアルタイムのオブジェクト検出を行います。

▼PCのインカメラ（もしくはUSBカメラ）を利用して顔検出を行う（顔検出のみ）  
https://github.com/se-lina/drone_tello/blob/main/real_time_face.py

▼PCのインカメラ（もしくはUSBカメラ）を利用して顔検出を行う（顔検出＋笑顔判定）  
https://github.com/se-lina/drone_tello/blob/main/real_time_face.py

#### リアルタイム顔検出（Telloのカメラに接続）
ここでは、Telloのカメラに接続し、リアルタイムのオブジェクト検出を行います。

▼顔検出のみ。Telloは飛ばない  
https://github.com/se-lina/drone_tello/blob/main/real_time_face_tello.py

## まとめ
今回の講義について、基礎編、応用編を記載しました。  
上記のプログラムを組み合わせする事により、より実用性のあるプログラムになると思います。  

例えば、ある一定の航路をを飛行させ、その航路の中に何人人がいたのかや、定期的な飛行および定点カメラを設置して、  
特定の場の人の往来などを検出、数を数えるプログラミングが出来るようになります。  
プログラムの基礎。そして、応用＋組み合わせでより良いプログラムに組み上がっていきます。  
現在ではChatGPT等を活用し、プログラムの作成方法やチェックもしてもらえるので、  
ぜひ、社会に役立てられるようなプログラム作りにチャレンジしてみてください。
