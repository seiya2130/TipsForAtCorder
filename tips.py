## 入力
### 数値を1文字ずつ数値リストにする
a = 123
sum(list(map(int, list(str(a))))) #### [1, 2, 3]

### 数値配列にする
a = 1 2 3
list(map(int, input().split())) #### [1, 2, 3]


## リスト
l = []

### 合計
from numpy import *
sum(l)

### 長さ
len(l)

### 最大値
max(l)

### 指定した値のインデックス
i = 1
l.index(i)

### 指定したインデックス要素の削除
del l[i]

## 昇順ソート
l.sort()

## 降順ソート
l.sort(reverse=True)


## 繰り返し  
### 1スタート
range(1, 3+1) # 1～4まで

