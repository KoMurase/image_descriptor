#_*_ coding: utf-8 _*_
import cv2
import matplotlib.pyplot as plt
#追加したライブラリ
import argparse
import numpy as np
###ヒストグラムに渡せていない

class ImageDescriptor:
    def __init__(self,histSize):
        self.histSize = histSize #クラスの変数に登録
        """
        画像を3x3に分割し、各ブロックで算出されたHSV色ヒストグラムを結合して返す関数.
        filename : 画像のファイルパス
        """
    def describe(self,filename):
        features = []
        im = filename
        height = 240
        width =320

        #縦の分割
        for h1 in range(3):
            #横の分割
            for w1 in range(3):
                w2 = w1 * height
                h2 = h1 * width
                print(w2,h2,width + w2,height + h2)
                c = im.crop((w2,h2,width + w2,height + h2))
                print(type(c))
                hist=np.bincount(c,minlength=256)
                features.append(hist)
        return features

    """def calc_hist(self,filename):
        im = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)#RGB空間からHSV空間に変換
        channels = [0,1,2]
        mask = None #画像マスクを使用しない
        histSize =[10,4,4]
        ranges = [0,180,0,256,0,256]
        hist = cv2.calcHist([im],channels,mask,histSize,ranges)"""

if __name__ == '__main__':
    histSize =[10,4,4]
    img_dsc = ImageDescriptor(histSize)
    filename = 'holidays/database/10.jpg'
    features = img_dsc.describe(filename)

    print('featuresのtypeは:',type(features))
    print(features)
    x = range(len(features))
    print('xのtypeは:',type(x))
    print('x =',x)
    plt.bar(x,features)
    plt.show()
