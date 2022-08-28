# ^(M-1) ≡ 1 (mod M) M:prime, 1 <= b < M
# b*modular ≡ 1 (mod M) ≡ b^(M-1)
# modular = b^(M-2) % M
# pythonではb^pの%Mはpow(b,p,M)でも可。つまりmodular=pow(b,M-2,M)でよい(繰り返し二乗法)

class MOD:
    def __init__(self,mod):
        self.mod = mod
        self.F = []
    def modpow(self,a,p):
        ans = 1
        while p>0:
            if p&1 : ans=ans*a%self.mod
            p>>=1
            a=a*a%self.mod
        return ans
    def modC(self,x,y):
        if self.F:
            fx,fy,fxy = self.F[x],self.F[y],self.F[x+y]
        else:
            fx,fy,fxy = 1,1,1
            for x in range(1,x+1) : fx = fx*x%self.mod
            for y in range(1,y+1) : fy = fy*y%self.mod
            for xy in range(1,x+y+1) : fxy = fxy*xy%self.mod
        deno = self.modpow(fx*fy%self.mod,self.mod-2)
        return fxy*deno%self.mod
    def modF(self,N):
        self.F = [1]*(N+1)
        for n in range(1,N+1) : self.F[n] = self.F[n-1] * n % self.mod
