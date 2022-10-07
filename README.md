# 競プロPythonLibrary自分用
提出しすぎてAtCoder提出歴から探すのが困難になってきたため作成
テスト環境:[[paiza]](https://paiza.io/ja/projects/new) [[atcoder]](https://atcoder.jp/contests/typical90/custom_test)

## アルゴリズム集
- [二分探索](/algorithm/BinarySearch.py)
- [動的計画法](/algorithm/DP.py)
- [貪欲法](/algorithm/Greedy.py)
- [グラフ理論](/algorithm/Graph.py)
- [行列](/algorithm/Linear.py)
- [モジュラ](/algorithm/Mod.py)
- [素数因数約数](/algorithm/Prime.py)
- [場合の数と確率期待値](/algorithm/CombinationEV.py)
- [再帰](/algorithm/Recursion.py)
- [幾何学](/algorithm/Vector.py)
- [bit演算諸々](/algorithm/Bit.py)

## データ構造集
- [階差と累積和](/struct/FDnCS.py)
- [木構造](/struct/tree.py)
- [UnionFind木](/struct/UF.py)
- [セグメント木(Fenwick,BIT)](/struct/Segment.py)
- DP行列化

## 頻出記述
~~~
# sys系
import sys
input = sys.stdin.readline # 文字列には使用不可
sys.setrecursionlimit(10**6)
sys.exit() # return 0
# 入力系
N=int(input())
N,M = map(int,input().split())
A = list(map(int,input().split()))
XY = [list(map(int,input().split())) for n in range(N)]
INF = 1<<60
# 文字入出力
S = list(map(lambda x:ord(x)-97,input().rstrip()))
atc, S = list(map(lambda c:ord(c)-97,"atcoder")), [] # atcoder文字列のunicode番list
[ S.append(atc.index(ord(c)-97)) if ord(c)-97 in atc else None for c in input() ] # 文字列をatcoderインデックスlistに変換
print("".join(map(lambda i:chr(i+97),ans)))
# 順列、部分集合
from itertools import permutations,combinations
permutations(list,subnum)
# 二分探索
from bisect import bisect_left,bisect
bisect_left(list,num)
min(abs(A[min(N-1,i)]-b),abs(A[max(0,i-1)]-b))
# 小数点以下切り上げ
(A+div-1) // div
~~~

## 計算量表
|logN|√N|**N**|NlogN|N<sup>2</sup>|N<sup>3</sup>|2<sup>N</sup>|N!|
|:----|:----|:----|:----|:----|:----|:----|:----|
|3|3|**5**|12|25|130|30|120|
|4|4|**10**|33|100|1,000|1,024|3,628,800|
|4|4|**15**|59|225|3.375|32,768|479,001,600|
|5|5|**20**|86|400|8,000|1,048,576|-|
|5|5|**25**|116|625|15,625|33,554,432|-|
|5|6|**30**|147|900|27,000|-|-|
|7|10|**100**|664|10,000|1,000,000|-|-|
|9|23|**500**|4,483|250,000|125,000,000|-|-|
|10|32|**1,000**|9,966|1,000,000|-|-|-|
|13|100|**10,000**|132,877|100,000,000|-|-|-|
|16|317|**100,000**|1,660,964|-|-|-|-|
|20|1,000|**1,000,000**|19,931,569|-|-|-|-|
|40|1,000,000|**10<sup>12</sup>**|-|-|-|-|-|
|60|10<sup>9</sup>|**10<sup>18</sup>**|-|-|-|-|-|

## 典型90問　[[問題]](https://atcoder.jp/contests/typical90)  [[解説]](https://github.com/E869120/kyopro_educational_90)
- [最少数え上げ要素を選択#25](https://atcoder.jp/contests/typical90/submissions/35225706)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/025.jpg)）
- [答え側を2分探索#1](https://atcoder.jp/contests/typical90/submissions/34487062)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/001.jpg)）
- [ダブリング(根付き木)#35](https://atcoder.jp/contests/typical90/submissions/35368779)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/035-02.jpg)）
- [桁DP#5](https://atcoder.jp/contests/typical90/submissions/33173921)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/005-01.jpg)）
- [部分集合はbitDP#45](https://atcoder.jp/contests/typical90/submissions/35441720)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/045.jpg)）
- [部分集合の場合の数は状態DP#8](https://atcoder.jp/contests/typical90/submissions/34868209)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/008.jpg)）
- [時限タスクは締切sortタスクx時間DP#11](https://atcoder.jp/contests/typical90/submissions/34888277)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/011-02.jpg)）
- [数列操作は区間DP#19](https://atcoder.jp/contests/typical90/submissions/35210132)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/019.jpg)）
- [辞書順は貪欲法#6](https://atcoder.jp/contests/typical90/submissions/34867193)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/006.jpg)）
- [連結判定はUnionFind#12](https://atcoder.jp/contests/typical90/submissions/34889083)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/012.jpg)）
- [加算と総和を繰返すにはFenwickTree#17](https://atcoder.jp/contests/typical90/submissions/35192768)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/017-03.jpg)）
- [更新と取得を繰返すにはSegmentTree#29#37](https://atcoder.jp/contests/typical90/submissions/35241803)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/029-02.jpg)）
- [素因数列挙はエラトステネスで非素数への加算#30](https://atcoder.jp/contests/typical90/submissions/35241997)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/030.jpg)）
- [各桁の数字の和＝Kの通り数は単調DP#42](https://atcoder.jp/contests/typical90/submissions/35427310)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/042.jpg)）
- [交互ゲームはgrundy数/dp/貪欲法#31](https://atcoder.jp/contests/typical90/submissions/35243279)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/031.jpg)）
- [連続区間は尺取法(単調増加なら二分探索も)#34](https://atcoder.jp/contests/typical90/submissions/35245981)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/034.jpg)）
- [マンハッタン距離は45度回転#36](https://atcoder.jp/contests/typical90/submissions/35370438)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/036.jpg)）
- [根付き木の距離は部下の数#39](https://atcoder.jp/contests/typical90/submissions/35374640)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/039.jpg)）
- [凸包×Pickの定理#41](https://atcoder.jp/contests/typical90/submissions/35426880)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/041-03.jpg)）
- [燃やす埋める問題は最大フロー#40](https://atcoder.jp/contests/typical90/submissions/35389500)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/040.jpg)）
