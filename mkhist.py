import cv2


filename = 'holidays/database/100.jpg'   #任意のg像ファイル
im = cv2.imread(filename,1)
#一つ目の引数は読み込みたい画像のファイルパス,
#二つ目の引数は0にするとグレースケール画像,1にするとカラー画像として読み込まれる

print(type(im))
#>><class 'numpy.ndarray'>
#ndarryはPythonの配列クラス

print(im.dtype)
#>> uint8
#uint8は符号型8ビット整数型のこと
print(im.shape)
#>>(192, 256, 3)
#192X256X3　の配列である　
#サイズが192X256でRGBの輝度値を並べたものである
print(im[150,200,:])
#150行200列目のRGB値[16 21 24]
print('\nヒストグラムの特徴を表示する')

im = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)#RGB空間からHSV空間に変換
channels = [0,1,2]
mask = None #画像マスクを使用しない
histSize =[10,4,4]
ranges = [0,180,0,256,0,256]
hist = cv2.calcHist([im],channels,mask,histSize,ranges)

print('Type :',type(hist))#histの変数タイプ確認

print('Shape :',hist.shape)#histのサイズ

print('HxSxVの行列をベクトルに変換して平滑化する.')

hist_vec = hist.flatten()
print('hist_vec.shape:',hist_vec.shape)
