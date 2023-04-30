# ここではコードの詳細説明を明記します。
モジュール、ライブラリのインストール方法は、別途、[module.md](https://github.com/se-lina/drone_tello/new/main/module.md)を参照ください。

## OpenCVを活用した静止画の顔検出

1. import cv2：OpenCVをインポートします。
1. face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')：顔検出用のカスケード分類器を読み込みます。この例では、 haarcascade_frontalface_default.xml というファイルを使用しています。
1. img = cv2.imread('image.jpg')：顔検出を行う画像を読み込みます。この例では、 image.jpg というファイルを使用しています。
1. gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)：読み込んだ画像をグレースケールに変換します。
1. faces = face_cascade.detectMultiScale(gray, 1.3, 5)：グレースケール画像から顔を検出します。この例では、 detectMultiScale() 関数に1.3と5の値を渡しています。
1. for (x, y, w, h) in faces:：検出された顔の座標を取得します。
1. cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)：検出された顔に矩形を描画します。 (x, y) は矩形の左上隅、 (x + w, y + h) は右下隅の座標を表します。 (0, 0, 255) は線の色を表し、この例では赤色になります。 2 は線の太さを表します。
1. cv2.imshow("Image", img)：結果を表示します。 cv2.waitKey(0) でキー入力を待機し、 cv2.destroyAllWindows() でウィンドウを閉じます。 

以上が静止画版のコードとその説明になります。

## OpenCVを活用した動画の顔検出


この例では、 cv2.VideoCapture() 関数を使用してビデオファイルを読み込み、 
cv2.CascadeClassifier() 関数で顔検出用のカスケード分類器を読み込んでいます。
ビデオファイルが正常に読み込まれた場合、 cap.read() 関数を使用してビデオファイルから1枚のフレームを読み込み、 
cv2.cvtColor() 関数でグレースケールに変換しています。
その後、 cv2.CascadeClassifier.detectMultiScale() 関数を使用して顔を検出し、 cv2.rectangle() 関数で検出された顔に矩形を描画しています。 

フレームの取得に失敗した場合はループを抜け、ビデオファイルの後処理を行います。また、 'q' キーが押された場合にもループを抜けてプログラムを終了します。
