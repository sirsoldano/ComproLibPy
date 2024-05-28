# 競プロPythonLibrary自分用
提出しすぎてAtCoder提出歴から探すのが困難になってきたため作成
- [アル数](https://atcoder.jp/contests/math-and-algorithm)（[解説](https://github.com/E869120/math-algorithm-book)）  
- [典型90](https://atcoder.jp/contests/typical90)（[解説](https://github.com/E869120/kyopro_educational_90)）
- [アル構](https://github.com/drken1215/book_algorithm_solution)
- [ライブラリ集(ついにマルチセット追加)](https://qiita.com/flour/items/e1a690c6b1c0a8b5c4b6)
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
- [Bitset](/struct/Bitset.py)
- [MultiSet(重複セット)](/struct/Multiset.py)
- [行標準形](/struct/RowCanonicalForm.py)
- [スライド](/struct/Slide.py)

## 頻出記述
#### 入力系
~~~
N=int(input())
N,M = map(int,input().split())
A = [*map(int,input().split())]
XY = [[*map(int,input().split())] for n in range(N)]
~~~
#### 文字列
~~~
alp,ALP = "abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ"
S = [*map(lambda x:ord(x)-97,input().rstrip())]
print("".join(map(lambda i:chr(i+97),ans))) # 大文字はord(c)-65
compressed = [(k, len(list(g))) for k,g in itertools.groupby(s)] # ランレングス圧縮
def palind(s): return sum(1 for n in range(len(s)//2) if s[n]!=s[-n-1])==0
~~~
#### 順列、部分集合
~~~
from itertools import permutations,combinations
permutations(list,subnum)
~~~
#### 二分探索
~~~
from bisect import bisect_left as bl
min(abs(A[min(N-1,i)]-b),abs(A[max(0,i-1)]-b))
~~~
#### 多重集合
~~~
# add,pop,clear,remove,discard,bisect_left,bisect_right,count,index
from sortedcontainers import SortedList
sl = SortedList()
~~~
#### 累積和
~~~
def cs(l):
    lsum = [l[0]]
    for n in range(1,len(l)) : lsum.append(lsum[-1]+l[n])
    return lsum
~~~
#### キュー
~~~
from collections import deque
q = deque()
q.append(s)
while q:
    pos = q.popleft()
import heapq as hq
q = []
hq.heappush(q,i)
hq.heappop(q)
~~~
#### 座標
~~~
# 探索方向
tera=((1,0),(0,1),(-1,0),(0,-1)) # x,y = y,-x でも可
octa=((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1))
tera={"U":(1,0),"R":(0,1),"D":(-1,0),"L":(0,-1)}
# 圧縮
sa = sorted(set(A))
cc = { v: i for i, v in enumerate(sa) }
~~~
#### 小数点以下切り上げ
~~~
(A+div-1) // div
-(-A//div)
~~~
#### グラフ
~~~
N,M = map(int,input().split())
edge,node=[[] for n in range(N)],[None]*N
for m in range(M):
    a,b = map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
~~~
<details>
<summary>dfs</summary>

~~~
#import sys; sys.setrecursionlimit(10**6); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def dfs(pos):
    node[pos] = 1
    for p in edge[pos]:
        if node[p] is None : dfs(p)
~~~
</details>
<details>
<summary>bfs</summary>

~~~
from collections import deque
def bfs(s,i):
    q,node[s] = deque(),i
    q.append(s)
    while q:
        pos = q.popleft()
        for p in edge[pos]:
            if node[p] is None:
                q.append(p)
                node[p]=i
i=0
for n in range(N):
    if node[n] == None:
        bfs(n,i)
        i+=1
~~~
</details>

#### 周期性利用
[競典58](https://atcoder.jp/contests/typical90/submissions/36319380)
[ABC167D](https://atcoder.jp/contests/abc167/submissions/50051923)
[ABC241E](https://atcoder.jp/contests/abc241/submissions/39758881)


<details>
<summary>
    
#### ローリングハッシュ
</summary>

[ABC141E](https://atcoder.jp/contests/abc141/submissions/46893571)
[基数表](https://gist.github.com/privet-kitty/295ac9202b7abb3039b493f8238bf40f#file-modulus-random-base-pair32-txt)
~~~
class RollingHash:
    def __init__(self,N,s,b1=998244353,b2=100000007,mod=1000000007):
        self.mod,self.b1,self.b2 = mod,b1,b2
        self.h1,self.h2 = [0]*(N+1),[0]*(N+1)
        self.r1,self.r2 = [pow(b1,n,mod) for n in range(1,N+1)],[pow(b2,n,mod) for n in range(1,N+1)]
        for n in range(N) : 
            self.h1[n+1] = (self.h1[n]*self.b1+s[n])%mod
            self.h2[n+1] = (self.h2[n]*self.b2+s[n])%mod
#(h1[l1+strlen]-r1*h1[l1])%mod==(h1[l2+strlen]-r1*h1[l2])%mod
def judge(l,r) : return (h1[r]-r1[r-l]*h1[l])%mod==(rh1[N-l]-r1[r-l]*rh1[N-r])%mod and (h2[r]-r2[r-l]*h2[l])%mod==(rh2[N-l]-r2[r-l]*rh2[N-r])%mod
~~~
</details>

<details>
<summary>
    
#### Z-algorithm
</summary>

[ABC257G](https://atcoder.jp/contests/abc257/tasks/abc257_g)
~~~
def z_algo(S):
    N,A = len(S),[0]*N
    i,j = 1,0
    A[0] = l = len(S)
    while i < l:
        while i+j < l and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A
~~~
</details>


#### 行列回転
~~~
# 90deg right
a = [[*x] for x in zip(*a[::-1])] # a[::-1]で上下逆、zip(*a)で転置
# 90deg left
a = [[*x] for x in [*zip(*a)][::-1]] # rightの逆順序
# 180deg
a = [a[n][::-1] for n in range(N)]
a = [x for x in a[::-1]]
# 転置
a = [[*x] for x in zip(*a)]
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
