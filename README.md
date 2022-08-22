# 競プロPythonLibrary自分用
提出しすぎてAtCoder提出歴から探すのが困難になってきたため作成

## アルゴリズム集
- 二分探索
- bit全探索
- 動的計画法
- 幅優先探索
- 深さ優先探索
- modpow
- bit演算
- 素数因数 [Prime.py](/algorithm/Prime.py)

## データ構造集
- 累積和
- DP行列化
- UnionFind木
- Fenwick木

## 頻出記述
~~~
# sys系
import sys
input = sys.stdin.readline # 文字列には使用不可
sys.setrecursionlimit(10**6)
sys.exit() # return 0
# 入力系
N,M = map(int,input().split()
A = list(map(int,input().split())
XY = [list(map(int,input().split()) for n in range(N)]
# 順列、部分集合
from itertools import permutations,combinations
permutations(list,subnum)
# 二分探索
from bisect import bisect_left,bisect
bitsect_left(list,num)
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
