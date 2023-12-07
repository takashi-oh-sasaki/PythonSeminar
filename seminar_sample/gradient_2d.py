import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


def _numerical_gradient_no_batch(f, x): #ｆは関数、NumPy配列ｘの各要素に対して数値微分
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x) #xと同じ形状で、要素が全て０の配列を生成：偏微分結果のテンポラリ
    
    for idx in range(x.size): 
        tmp_val = x[idx] #1周目はx[0]、2週目はx[1]
        
        x[idx] = float(tmp_val) + h # f(x+h)
        fxh1 = f(x)  
        x[idx] = tmp_val - h   # f(x-h)
        fxh2 = f(x)
        
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val  # x[0]、x[1]での偏微分の計算結果を元に戻す
        
    return grad

def numerical_gradient(f, X): #numpy配列ｘの各要素に対し数値微分
    if X.ndim == 1: #ｘが1次元だったら
        return _numerical_gradient_no_batch(f, X) #そのまま数値微分
    else:
        grad = np.zeros_like(X) #xと同じ形の空行列を作成
        
        for idx, x in enumerate(X): #enumerate()：各要素に分解するとともにインデックスを付ける関数
            grad[idx] = _numerical_gradient_no_batch(f, x) #xが2次元以上の場合、こちら
        
        return grad

def function_2(x):
    if x.ndim == 1: #ndim：多次元配列が何次元の構造をしているのか
        return np.sum(x**2)
    else:
        return np.sum(x**2, axis=1) #行方向がaxis=0、列方向がaxis=1、奥行き方向がaxis=2

print(numerical_gradient(function_2,np.array([3.0,4.0]))) #（3.0,4.0）での勾配はベクトル（6.,8.）

if __name__ == '__main__': #このブロックにはメインプログラムとして実行されたときだけ動作すべきコードが書いてある
    x0 = np.arange(-2, 2.5, 0.25) 
    x1 = np.arange(-2, 2.5, 0.25)
    X, Y = np.meshgrid(x0, x1)
    
    X = X.flatten() #n次元のnumpy配列を1次元に変換
    Y = Y.flatten()

    grad = numerical_gradient(function_2, np.array([X, Y]).T).T #.T：転置

    plt.figure()
    plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666") #勾配の結果にマイナスをつけたベクトルを描画
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.xlabel('x0')
    plt.ylabel('x1')
    plt.grid()
    plt.draw()
    plt.show()