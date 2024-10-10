# 競プロPythonLibrary自分用
- [アル数](https://atcoder.jp/contests/math-and-algorithm)（[解説](https://github.com/E869120/math-algorithm-book)）  
- [典型90](https://atcoder.jp/contests/typical90)（[解説](https://github.com/E869120/kyopro_educational_90)）
- [アル構](https://github.com/drken1215/book_algorithm_solution)
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
<details>
<summary>

##### 一致区間探索
</summary>

##### Z-algorithm
[ABC257G](https://atcoder.jp/contests/abc257/tasks/abc257_g)
[解説](https://qiita.com/Pro_ktmr/items/16904c9570aa0953bf05)
~~~
def z_algo(S):
    N = len(S)
    res = [N]+[0]*(N-1)
    i=1;j=0
    while i<N:
        while i+j<N and S[j]==S[i+j]:
            j+=1
        if j==0:
            i+=1
            continue
        res[i]=j
        k = 1
        while i+k < N and res[k]+k < j:
            res[i+k] = res[k]
            k += 1
        i += k; j -= k
    return res
~~~
##### ローリングハッシュ
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

#### 二分探索
~~~
from bisect import bisect_left as bl
min(abs(A[min(N-1,i)]-b),abs(A[max(0,i-1)]-b))
def binsearch(l,r):
    while r-l>1:
        m = (l+r)//2
        if judge(m) : l=m
        else : r=m
    return l
~~~
#### 累積和
~~~
def cs(l):
    lsum = [0]
    for n in range(len(l)) : lsum.append(lsum[-1]+l[n])
    return lsum
def imos(A):
    N = max(r for l,r,h in A)+1
    updn = [0]*(N+1)
    for l,r,h in A : updn[l]+=h;updn[r+1]-=h
    cs = [updn[0]]+[0]*(N-1)
    for n in range(1,N) : cs[n]=cs[n-1]+updn[n]
    return cs
# CS2d
for l in range(1,N+1):
    for r in range(1,N+1) : lr[l][r]+=lr[l][r-1] + a[l-1][r-1]
    for r in range(1,N+1) : lr[l][r]+=lr[l-1][r]
cssum = lr[r1][r2]-lr[r1][l2-1]-lr[l1-1][r2]+lr[l1-1][l2-1]
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
#### モジュラ
~~~
class MOD:
    def __init__(self,mod,N=4000001):
        self.mod,self.fac,self.finv,self.inv = mod,[0]*N,[0]*N,[0]*N
        self.fac[0] = self.fac[1] = self.finv[0] = self.finv[1] = self.inv[1] = 1
        for i in range(2,N):
            self.fac[i] = self.fac[i-1]*i%mod
            self.inv[i] = mod-self.inv[mod%i]*(mod//i)%mod
            self.finv[i] = self.finv[i-1]*self.inv[i]%mod
#    def modC(self,X,Y) : return self.fac[X+Y]*self.finv[X]%self.mod*self.finv[Y]%self.mod
    def C(self,n,k) : return self.fac[n]*self.finv[n-k]%self.mod*self.finv[k]%self.mod
    def P(self,n,k) : return self.fac[n]*self.finv[n-k]%self.mod
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
# maze
ans = [[-1]*W for h in range(H)]
q = deque([(sh,sw)])
ans[sh][sw] = 0
tera=((1,0),(0,1),(-1,0),(0,-1))
while q:
    h,w = q.popleft()
    for dh,dw in tera:
        if 0<=h+dh<H and 0<=w+dw<W and ans[h+dh][w+dw]==-1 and mp[h+dh][w+dw]==".":
            q.append((h+dh,w+dw))
            ans[h+dh][w+dw] = ans[h][w]+1
print(ans[gh][gw])
~~~
</details>

<details>
<summary>dijkstra</summary>

~~~
N,M = map(int,input().split())
edge,node=[[] for n in range(N)],[1<<60]*N
for m in range(M):
    a,b,c = map(int,input().split())
    edge[a-1].append((b-1,c))
    edge[b-1].append((a-1,c))
from heapq import heappush, heappop
def dijkstra(s):
    q = []
    heappush(q,(0,s))
    while len(q)>0 :
        dist,pos = heappop(q)
        if node[pos] < 1<<60 : continue
        node[pos] = dist
        for p,d in edge[pos]:
            if node[p] > dist+d:
                heappush(q,(dist+d,p))
~~~
</details>

#### セグ木

<details>
<summary>セグ木</summary>

~~~
class SegT:
    def __init__(self,N,func,default):
        self.default = default
        self.func = func
        self.slen = 1
        while(self.slen<N) : self.slen<<=1
        self.st = [self.default] * (self.slen*2)
    def update(self,i,x):
        i += self.slen
        self.st[i] = x
        while i>=2 :
            i>>=1
            self.st[i] = self.func(self.st[i*2],self.st[i*2+1])
    def get(self,l,r):
        l += self.slen; r += self.slen
        res = self.default
        while l < r:
            if l & 1 : 
                res = self.func(res, self.st[l])
                l += 1
            if r & 1: 
                r -= 1 
                res = self.func(res, self.st[r])
            l >>= 1; r >>= 1
        return res
~~~
</details>

<details>
<summary>遅延セグ木</summary>

~~~
from atcoder.lazysegtree import LazySegTree
def op(s1,s2) : return max(s1,s2)
def mp(f,s) : return s+f
def comp(f2,f1) : return f1+f2
lst = LazySegTree(op,0,mp,comp,0,[0 for n in range(200001)])
~~~
</details>

#### UnionFind

<details>
<summary>基本UF</summary>

~~~
class UnionFind:
    def __init__(self,n):
        self.uft = [-1]*n
        self.rank = [0]*n
    def root(self,pos):
        if self.uft[pos] == -1 : return pos
        self.uft[pos]=self.root(self.uft[pos])
        return self.uft[pos]
    def union(self,a,b):
        ra,rb = self.root(a),self.root(b)
        if ra==rb : return
        if self.rank[ra] < self.rank[rb] :
            self.uft[ra] = rb
        else :
            self.uft[rb] = ra
            if self.rank[ra]==self.rank[rb] : self.rank[ra]+=1
    def same(self,a,b):
        return self.root(a)==self.root(b)
~~~
</details>

<details>
<summary>クラスカル法</summary>

~~~
items.sort()
ans,cnt=0,0
for c,l,r in items :
    if uf.same(l,r)==False:
        uf.union(l,r)
        ans, cnt = ans+c, cnt+1
if cnt==N : print(ans)

# heapq ver
import heapq as hq
ans,cnt=0,1
uf = UnionFind(N)
while e:
    c,l,r=hq.heappop(e)
    if uf.same(l,r)==False:
        uf.union(l,r)
        ans, cnt = ans+c, cnt+1
if cnt==N : print(ans)
else : print(-1)
~~~
</details>


#### 周期性利用、ダブリング

[競典58](https://atcoder.jp/contests/typical90/submissions/36319380)
[ABC167D](https://atcoder.jp/contests/abc167/submissions/50051923)
[ABC241E](https://atcoder.jp/contests/abc241/submissions/39758881)
~~~
N,K = map(int,input().split())
A = [*map(lambda x:int(x)-1,input().split())]
dub = [A]+[[None]*N for d in range(59)]
for d in range(1,60):
    for n in range(N):
        dub[d][n] = dub[d-1][dub[d-1][n]]
for n in range(N):
    v = n
    for d in range(60):
        if K&(1<<d) : 
            v=dub[d][v]
~~~

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
