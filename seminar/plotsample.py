import numpy as np
from matplotlib import pyplot as plt
 
#2入力パーセプトロンの関数
def perceptron(x1, x2, w1, w2, theta):
    f = w1 * x1 + w2 * x2
    if f <= theta:
        y = 0
    else:
        y = 1
    return y
 
x1 = np.array([0, 0, 1, 1, 0, 1, -1, -1, -1, 2, 0, 2, 1, 2, -1, 2])
x2 = np.array([0, 1, 0, 1, -1, -1, 0, -1, 1, 0, 2, 1, 2, 2, 2, -1])
w1 = 0.5
w2 = 0.5
theta = 0.2
 
#プロット用の配列（P0がy=0, P1がy=1の座標を入れるための配列）
P0_x = []
P0_y = []
P1_x = []
P1_y = []
 
#プロット用にデータを分類し格納する。
for i in range(16):
    X1 = x1[i]
    X2 = x2[i]
    y = perceptron(X1, X2, w1, w2, theta)
    print(y)
    if y == 0:
        P0_x.append(x1[i])
        P0_y.append(x2[i])
    else:
        P1_x.append(x1[i])
        P1_y.append(x2[i])
 
P0_x = np.array(P0_x)
P0_y = np.array(P0_y)
P1_x = np.array(P1_x)
P1_y = np.array(P1_y)
 
# ここからグラフ描画
# フォントの種類とサイズを設定する。
plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'Times New Roman'
 
# 目盛を内側にする。
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
 
# グラフの上下左右に目盛線を付ける。
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.yaxis.set_ticks_position('both')
ax1.xaxis.set_ticks_position('both')
 
# 軸のラベルを設定する。
ax1.set_xlabel('$x_{1}$')
ax1.set_ylabel('$x_{2}$')
 
# データの範囲と刻み目盛を明示する。
ax1.set_xticks(np.arange(-3, 3, 1))
ax1.set_yticks(np.arange(-3, 3, 1))
ax1.set_xlim(-1.5, 2.5)
ax1.set_ylim(-1.5, 2.5)
 
# データプロットの準備とともに、ラベルと線の太さ、凡例の設置を行う。
ax1.scatter(P0_x, P0_y, facecolors = 'none', edgecolors = 'r', label='$y=0$', lw=1)
ax1.scatter(P1_x, P1_y, label='$y=1$', lw=1)
 
fig.tight_layout()
 
# グラフを表示する。
plt.show()
plt.close()