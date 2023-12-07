# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 親ディレクトリのファイルをインポートするための設定
import numpy as np
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

# データの読み込み
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 10000  # 繰り返しの回数を適宜設定する
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1) #60000データ、100ミニバッチ、600回＝1エポック、繰り返し10000回：16.67エポックで完了

for i in range(iters_num):
    #ステップ１ミニバッチの取得：毎回やる
    batch_mask = np.random.choice(train_size, batch_size) 
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    # ステップ２勾配の計算
    #grad = network.numerical_gradient(x_batch, t_batch) #勾配法
    grad = network.gradient(x_batch, t_batch) #誤差逆伝播法
    
    # ステップ３パラメータの更新
    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key] #学習
    
    #学習経過の記録
    loss = network.loss(x_batch, t_batch) #損失関数の値を求める
    train_loss_list.append(loss)
    
    # 途中経過を表示
    #print('iter ' + str(i + 1) + ' (' + str(np.round((i + 1) / iters_num * 100, 1)) + '%) ') # 繰り返し
    #print('loss : ' + str(loss))
    
    if i % iter_per_epoch == 0: #１エポック終わったら結果表示
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        
        print(f"[更新数]{i: >4} [損失関数の値]{loss:.4f} "
              f"[訓練データの認識精度]{train_acc:.4f} [テストデータの認識精度]{test_acc:.4f}")

fig = plt.figure()
axes= fig.subplots(2)
       
# グラフの描画　認識制度の推移
markers = {'train': 'o', 'test': 's'}
x1 = np.arange(len(train_acc_list))
axes[0].plot(x1, train_acc_list, label='train acc')
axes[0].plot(x1, test_acc_list, label='test acc', linestyle='--')
axes[0].set_xlabel("epochs")
axes[0].set_ylabel("accuracy")
axes[0].set_ylim(0, 1.0)
axes[0].legend(loc='lower right')

# グラフの描画　損失関数の推移
x2 = np.arange(len(train_loss_list))
axes[1].plot(x2, train_loss_list, label='train_loss')
axes[1].set_xlabel("iter")
axes[1].set_ylabel("train_loss")
axes[1].set_ylim(0, 3.0)
axes[1].legend(loc='upper right')

plt.show()