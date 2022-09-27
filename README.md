# 競プロPythonLibrary自分用
提出しすぎてAtCoder提出歴から探すのが困難になってきたため作成

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
- [セグメント木(Fenwick,BIT)](/struct/SegmentTree.py)
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

## 典型90問
- [答え側を2分探索](https://atcoder.jp/contests/typical90/submissions/34487062)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/001.jpg)）
- [桁DP](https://atcoder.jp/contests/typical90/submissions/33173921)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/005-01.jpg)）
- [部分集合の場合の数は状態DP](https://atcoder.jp/contests/typical90/submissions/34868209)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/008.jpg)）
- [時限タスクは締切sortタスクx時間DP](https://atcoder.jp/contests/typical90/submissions/34888277)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/011-02.jpg)）
- [辞書順は貪欲法](https://atcoder.jp/contests/typical90/submissions/34867193)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/006.jpg)）
- [連結判定はUnionFind](https://atcoder.jp/contests/typical90/submissions/34889083)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/012.jpg)）
- [加算と総和を繰返すにはFenwickTree](https://atcoder.jp/contests/typical90/submissions/35192768)（[解説](https://github.com/E869120/kyopro_educational_90/blob/main/editorial/017-03.jpg)）
