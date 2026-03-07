from collections import Counter
class Atkin:
    def __init__(self,n=10**7):
        self.primes,self.minfac,p = [],[i for i in range(n+1)],2
        for p in range(2,n+1):
            if self.minfac[p]==p : self.primes.append(p)
            for i in self.primes :
                if i*p>n or self.minfac[p] < i : break
                self.minfac[i*p] = i
    def get_pf(self,x):
        pf = Counter()
        while x>1:
            pf[self.minfac[x]]+=1
            x //= self.minfac[x]
        return pf
from collections import Counter
class Eratos:
    def __init__(self,n=10**7):
        self.primes,self.minfac,self.mobius,p = [],[i for i in range(n+1)],[1]*(n+1),2
        while p<=n:
            if self.minfac[p]==p:
                self.primes.append(p)
                self.mobius[p] = -1
                for i in range(2,n//p+1) : 
                    if self.minfac[i*p] == i*p : self.minfac[i*p]=p
                    if i%p==0 : self.mobius[i*p] = 0
                    else : self.mobius[i*p] = -self.mobius[i*p]
            p+=1
    def get_pf(self,x):
        pf = Counter()
        while x>1:
            pf[self.minfac[x]]+=1
            x //= self.minfac[x]
        return pf
    def get_divs(self,x):
        pf = self.get_pf(x)
        divs = [1]
        for p in sorted(pf):
            for i in range(len(divs)):
                mul = 1
                for j in range(pf[p]):
                    mul *= p
                    divs.append(divs[i]*mul)
        return sorted(divs)
    def fastzeta(self,f):
        N = len(f)
        for p in range(2,N):
            if self.minfac[p]!=p : continue
            for i in range((N-1)//p,0,-1):
                f[i] += f[i*p]
    def fastmobius(self,f):
        N = len(f)
        for p in range(2,N):
            if self.minfac[p]!=p : continue
            for i in range(1,(N-1)//p+1):
                f[i] -= f[i*p]

# 約数の個数を事前列挙
# tc : NlogN
# ul : 10^7
def divisors(N):
    div = [0,1]+[2]*(N-1)
    for n in range(2,N//2+1):
        i=2
        while n*i<=N:
            div[n*i]+=1
            i+=1
    return div
#約数の列挙
# tc : √N
# ul : 10^12
def divs(n):
    ldiv , udiv = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            ldiv.append(i)
            if i != n // i:
                udiv.append(n//i)
        i += 1
    return ldiv + udiv[::-1]
# tc : √N
# ul : 10^12
from collections import deque,Counter
def tridiv(n):
    pf, f = Counter(), 2
    while f*f<=n:
        if n%f == 0 :
            pf[f]+=1
            n//=f
        else : f = f+2 if f>2 else 3
    if n>1 : 
        pf[n]+=1
    return pf
# 複数回実行する場合は事前に素数列挙
# tc : 素数の数はlogN
# PL=eratos(int(n**0.5))
def tridiv(n):
    pf, ind = [], 0
    while ind<len(PL) and PL[ind]*PL[ind]<=n:
        if n%PL[ind] == 0 :
            pf.append(PL[ind])
            n//=PL[ind]
        else : ind+=1
    if n>1 : pf.append(n)
    return pf

#GCD
# tc : log(A+B)
# ul : over 10^18
def gcd(A,B):
    while A>=1 and B>=1 :
        if(A>B) : A = A%B
        else : B = B%A
    return A if A else B
def gcd(A,B):
    if B==0 : return A
    else : return gcd(B,A%B)
# use library
import math
math.gcd(A,B)
lcm = A*B//math.gcd(A,B)

# 倍数の集合 ( N//lcm を集合個数奇数個は加算、偶数個は減算してbit全探索)
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_be
for b in range(1,(1<<K)):
    cnt, lcm = 0, 1
    for k in range(K) : 
        if b&(1<<k) : cnt, lcm = cnt+1, lcm*A[k]//math.gcd(lcm,A[k])
    ans = ans + N//lcm if cnt%2 else ans - N//lcm

# 拡張ユークリッドの互助法　https://qiita.com/luuguas/items/1c0bc4fb7a5d8c7f3c07
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0
# 中国剰余定理
def remainder(V):
    x = 0; d = 1
    for X, Y in V:
        g, a, b = extgcd(d, Y)
        x, d = (Y*b*x + d*a*X) // g, d*(Y // g)
        x %= d
    return x, d
# 一次不定方程式　https://qiita.com/DaikiSuyama/items/3687e9f2fa3ed097e2fc
class LDE:
    def __init__(self,a,b,c):
        self.a,self.b,self.c=a,b,c
        self.m,self.x,self.y=0,0,0
        g,self.x,self.y = self.extgcd(abs(self.a),abs(self.b))
        if c%g!=0:
            self.check=False
        else:
            self.check=True
            if a<0:self.x=-self.x
            if b<0:self.y=-self.y
            self.x = self.x*c//g
            self.y = self.y*c//g
            self.a //= g
            self.b //= g
    def extgcd(self,a, b):
        if b:
            d, y, x = self.extgcd(b, a % b)
            y -= (a // b) * x
            return d, x, y
        return a, 1, 0
    def get(self):
        if self.check==False : return None
        else : return self.x,self.y
    def m_update(self,m):
        self.x+=(m-self.m)*self.b
        self.y-=(m-self.m)*self.a
        self.m=m
# ax+by=cの最小の自然数回答
lde = LDE(a,b,c)
ans = lde.get()
if ans is None : print(-1)
else:
  x,y = ans
  a,b = lde.a,-lde.b
  lde.m_update(min((x-1)//a,(y-1)//b)) # 非負整数であればx-1,y-1 → x,y
  ans = lde.get()
