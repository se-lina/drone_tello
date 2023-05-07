# ここではコードの詳細説明を明記します。
モジュール、ライブラリのインストール方法は、別途、[module.md](https://github.com/se-lina/drone_tello/new/main/module.md)を参照ください。  
基本的には、MacOS上でTelloにUDP接続（1on1のWiFi）し、VS codeでプログラムを確認・変数の変更をしながら進めます。  
ファイル構造やディレクトリ構造は適宜自分のパソコンに合わせて変更してください。

## OpenCVを活用した静止画の顔検出

1. import cv2：OpenCVをインポートします。
1. face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')：顔検出用のカスケード分類器を読み込みます。この例では、 haarcascade_frontalface_default.xml というファイルを使用しています。
1. img = cv2.imread('image.jpg')：顔検出を行う画像を読み込みます。この例では、 image.jpg というファイルを使用しています。
1. gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)：読み込んだ画像をグレースケールに変換します。
1. faces = face_cascade.detectMultiScale(gray, 1.3, 5)：グレースケール画像から顔を検出します。この例では、 detectMultiScale() 関数に1.3と5の値を渡しています。
1. for (x, y, w, h) in faces:：検出された顔の座標を取得します。
1. cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)：検出された顔に矩形を描画します。 (x, y) は矩形の左上隅、 (x + w, y + h) は右下隅の座標を表します。 (0, 0, 255) は線の色を表し、この例では赤色になります。 2 は線の太さを表します。
1. cv2.imshow("Image", img)：結果を表示します。 cv2.waitKey(0) でキー入力を待機し、 cv2.destroyAllWindows() でウィンドウを閉じます。 



## OpenCVを活用した動画の顔検出


この例では、 cv2.VideoCapture() 関数を使用してビデオファイルを読み込み、 
cv2.CascadeClassifier() 関数で顔検出用のカスケード分類器を読み込んでいます。
ビデオファイルが正常に読み込まれた場合、 cap.read() 関数を使用してビデオファイルから1枚のフレームを読み込み、 
cv2.cvtColor() 関数でグレースケールに変換しています。
その後、 cv2.CascadeClassifier.detectMultiScale() 関数を使用して顔を検出し、 cv2.rectangle() 関数で検出された顔に矩形を描画しています。 

フレームの取得に失敗した場合はループを抜け、ビデオファイルの後処理を行います。また、 'q' キーが押された場合にもループを抜けてプログラムを終了します。


## その他
### YOLOについて
YOLO (You Only Look Once) は、物体検出のためのディープラーニングアルゴリズムです。  
YOLOは、画像全体を一度に処理して、画像内の物体を同時に検出することができます。  
YOLOは、高速で精度の高い物体検出が可能であり、リアルタイムアプリケーションに適しています。  
  
YOLOは、畳み込みニューラルネットワーク (CNN) を使用して実装されており、画像内の物体の種類と位置を同時に推定します。  
YOLOは、物体の位置とサイズを予測するために、画像をグリッドに分割し、各グリッドに対して複数のバウンディングボックスを予測します。  
そして、各バウンディングボックスに対して、物体のクラスの確率を予測します。  
最終的に、各バウンディングボックスの予測された物体クラスの確率と、バウンディングボックスの位置とサイズを組み合わせて、物体検出を行います。
  
YOLOは、軽量化されたバージョンであるTiny YOLOや、高精度なバージョンであるYOLOv3などが存在し、多様なアプリケーションに適用されています。
