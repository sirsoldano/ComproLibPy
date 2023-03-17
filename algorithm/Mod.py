# ^(M-1) ≡ 1 (mod M) M:prime, 1 <= b < M
# b*modular ≡ 1 (mod M) ≡ b^(M-1)
# modular = b^(M-2) % M
# pythonではb^pの%Mはpow(b,p,M)でも可。つまりmodular=pow(b,M-2,M)でよい(繰り返し二乗法)

class MOD:
    def __init__(self,mod):
        self.mod = mod
        self.F = []
        self.Finv = []
    def modpow(self,a,p):
        ans = 1
        while p>0:
            if p&1 : ans=ans*a%self.mod
            p>>=1
            a=a*a%self.mod
        return ans
    def modC(self,X,Y):
        if self.F:
            return self.F[X+Y]*self.Finv[X]%self.mod*self.Finv[Y]%self.mod
        else:
            fx,fy,fxy = 1,1,1
            for x in range(1,X+1) : fx = fx*x%self.mod
            for y in range(1,Y+1) : fy = fy*y%self.mod
            for xy in range(1,X+Y+1) : fxy = fxy*xy%self.mod
            deno = self.modpow(fx*fy%self.mod,self.mod-2)
            return fxy*deno%self.mod
    def modF(self,N):
        self.F = [1]*(N+1)
        for n in range(1,N+1) : self.F[n] = self.F[n-1] * n % self.mod
        self.Finv = [0]*(N+1)
        for n in range(0,N+1) : self.Finv[n] = self.modpow(self.F[n], self.mod-2)


class MOD:
    def __init__(self,mod):
        self.mod = mod
        self.fac = [0]*100000
        self.finv = [0]*100000
        self.inv = [0]*100000
        self.fac[0] = self.fac[1] = self.finv[0] = self.finv[1] = self.inv[1] = 1
        for i in range(2,100000):
            self.fac[i] = self.fac[i-1]*i%mod
            self.inv[i] = mod-self.inv[mod%i]*(mod//i)%mod
            self.finv[i] = self.finv[i-1]*self.inv[i]%mod
    def modC(self,X,Y):
        return self.fac[X+Y]*self.finv[X]%self.mod*self.finv[Y]%self.mod
