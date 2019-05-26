import cv2
import argparse
import sys
from PIL import Image

def display(filename):
    im = cv2.imread(filename,1)#画像の読み込み
    if im is None:   #エラー処理
        print(filename, 'does not exist!')
        sys.exit('Error')
    height,width = im.shape[0:2]    #画像サイズを取得
    print('height:',height,'width:',width)   #画像サイズ表示
    cv2.imshow(filename, im)
    cv2.waitKey(0)    #キー入力待機
    cv2.destoryAllWindows()   #すべてのウィンドウズを閉じる


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i","--image",required=True,help="Path to the image")
    args = vars(ap.parse_args())
    display(filename=args['image'])
