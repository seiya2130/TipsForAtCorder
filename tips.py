## 入力
### 数値を1文字ずつ数値リストにする
a = 123
sum(list(map(int, list(str(a))))) #### [1, 2, 3]

### 数値配列にする
a = 1 2 3
list(map(int, input().split())) #### [1, 2, 3]

### 各変数にする
a = 1 2
n, sum = map(int, input().split()) ### n=1 sum=2


## 出力
### 変数(複数)
a = 1
b = 2
print(a, b) ### 1 2

### リスト
l = [1, 2, 3]
print(*l) ### 1 2 3 


## リスト
l = []

### 合計
from numpy import *
sum(l)

### 長さ
len(l)

### 最大値
max(l)

### 要素の追加
l.append(1)

### 指定した値のインデックス
i = 1
l.index(i)

### 指定したインデックス要素の削除
del l[i]

### 昇順ソート
l.sort()

### 降順ソート
l.sort(reverse=True)

### 重複削除(その後リストにする)
list(set(l))


## 繰り返し

## 0スタート
range(3) # 0,1,2

### 1スタート
range(1, 3) # 1,2

### 1スタートで最後+1
range(1, 3+1) # 1,2,3


## 文字列
### 後方一致
"abc".endswith("bc") # True

### 後方から一致文字を削除
"abc".rstrip("c") # ab


## 数値
### 割り算(余り切り捨て)
5 // 2 ### 2

### 累乗
4 ** 3 ### 64