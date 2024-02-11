# tc : NloglogN
# ul : 10^7
def eratos(N):
    prime,is_prime,p = [],[0,0]+[1]*(N-1),2
    while p<=N:
        if is_prime[p]:
            prime.append(p)
            for i in range(2,N//p+1) : is_prime[i*p]=0
        p+=1
    return prime
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
def tridiv(n):
    pf, f = dict(), 2
    while f*f<=n:
        if n%f == 0 :
            if f not in pf : pf[f]=0
            pf[f]+=1
            n//=f
        else : f = f+2 if f>2 else 3
    if n>1 : 
        if n not in pf : pf[n]=0
        pf[n]+=1
    return pf
# 複数回実行する場合は事前に素数列挙
# PL=eratos(int(n**0.5))
def tridivPL(n,PL):
    pf, ind = [], 0
    while ind<len(PL) and PL[ind]*PL[ind]<=n:
        if n%PL[ind] == 0 :
            pf.append(PL[ind])
            n//=PL[ind]
        else : ind+=1
    if n>1 : pf.append(n)
    return pf

import collections
collections.Counter(tridiv(int(input())))

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

# 拡張ユークリッドの互助法
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
# 一次不定方程式
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
