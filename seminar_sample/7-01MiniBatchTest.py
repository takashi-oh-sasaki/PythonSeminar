# coding: utf-8
import numpy as np
import os
import pickle
import sys
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True,one_hot_label=True)

print(x_train.shape) #60000,784 60000枚、784ピクセル
print(t_train.shape) #60000,10  教師データは10列

train_size=x_train.shape[0] #trainのサイズ取得->60000
batch_size=10 #x_trainから何個取り出す？->10
batch_mask=np.random.choice(train_size,batch_size) #60000のなかから10取り出す
x_batch=x_train[batch_mask]
t_batch=t_train[batch_mask]

print(batch_mask)

#ここから描画
def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

img = x_batch[0]
for j in range(1, batch_size):
    img = np.concatenate((img, x_batch[j]), axis=0)
img *= 255
img_show(img.reshape(28 * batch_size, 28))





