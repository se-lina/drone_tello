# この講義で必要なインストールモジュール

## OpenCV ライブラリ

OpenCVをインストールするために必要な依存関係をインストールする
OpenCVをインストールするためには、依存関係をインストールする必要があります。以下のコマンドを使用して、必要な依存関係をインストールできます。

```
$ sudo apt-get update
$ sudo apt-get install python3-opencv
```
上記のコマンドはUbuntuでのインストール方法ですが、他のディストリビューションやオペレーティングシステムでも同様の手順を踏むことができます。

OpenCVをPythonに統合する
OpenCVをPythonで使用するには、PythonにOpenCVを統合する必要があります。これには、以下のコマンドを使用してPythonのパッケージ管理ツールであるpipを使用してインストールできます。
```
$ pip install opencv-python
```
上記のコマンドでOpenCVがインストールされ、PythonからOpenCVを利用することができます。  


#### OpenCVの拡張
また、 opencv-contrib-python パッケージをインストールすることで、OpenCVの機能を拡張することができます。  
以下が手順になります。   
コマンドプロンプトまたはターミナルを開きます。  
```
pip install opencv-contrib-python
```
と入力し、Enterキーを押します。


## DJI Tello ライブラリ

Telloを制御するためには、以下の手順が必要です。   
Python 3をインストールしたパソコンにdjitellopyライブラリをインストールします。  
以下のコマンドを使用して、pipを使用してインストールできます。 
```
pip install djitellopy  
```

TelloドローンをWi-Fiで接続します。  

djitellopyをインポートして、Telloオブジェクトを作成します。 

以下は、サンプルコードです。 
```
from djitellopy import Tello  
  
tello = Tello()  
  
tello.connect()  
tello.takeoff()  
  
tello.move_left(50)  
tello.rotate_counter_clockwise(90)  
tello.move_forward(100)  
  
tello.land()  
```
これで、Telloドローンを制御するPythonプログラムを書くことができます。



## git

```
$ sudo apt install git
```


## pip
pip installが出来ないときは講師、TA,SAに聞いてください。  
パソコンにpipがインストールされていないか、python3またはpip3で動くときがあります。


## TelloをWiFiルーター経由で操作

TelloをWiFiルーター経由で操作するためには、以下の手順を実行する必要があります。  
WiFiルーターに接続する: TelloをWiFiルーターに接続します。  
これにより、Telloとコンピューターまたはスマートフォンが同じネットワークに接続されます。 
TelloのIPアドレスを取得する: TelloのIPアドレスを取得するには、TelloをPCに接続し、  
Telloへのpingを実行します。以下のコマンドを使用して、Telloにpingを送信できます。 
```
ping -c 2 192.168.10.1  
```

このコマンドで、TelloのIPアドレスが192.168.10.1であることがわかります。  
Telloコマンドポートの開放: TelloをWiFiルーター経由で操作するためには、Telloコマンドポート（デフォルトでは8889ポート）を開放する必要があります。  
ルーターの設定画面から、ポートフォワーディングを設定して、TelloのIPアドレスとポート番号8889を指定します。  
コンピューターまたはスマートフォンでTello SDKを使用: Tello SDKを使用して、コンピューターまたはスマートフォンからTelloを操作することができます。  
SDKを使用する前に、SDKライブラリをインストールし、djitellopyなどのライブラリを使用して、Telloを制御するPythonスクリプトを作成する必要があります。   

以上の手順を実行することで、WiFiルーター経由でTelloを制御することができます。  
ただし、ルーターの設定によっては、ポートフォワーディングが正しく機能しない場合があります。  
その場合は、ルーターの設定を確認して、ポートフォワーディングが正しく設定されていることを確認してください。
