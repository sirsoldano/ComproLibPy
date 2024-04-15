# ^(M-1) ≡ 1 (mod M) M:prime, 1 <= b < M
# b*modular ≡ 1 (mod M) ≡ b^(M-1)
# modular = b^(M-2) % M
# pythonではb^pの%Mはpow(b,p,M)でも可。つまりmodular=pow(b,M-2,M)でよい(繰り返し二乗法)
# modular=pow(b,-1,M)も可

class MOD: # for single use
    def __init__(self,mod):
        self.mod = mod
        self.F = []
        self.Finv = []
    def modC(self,X,Y):
        fx,fy,fxy = 1,1,1
        for x in range(1,X+1) : fx = fx*x%self.mod
        for y in range(1,Y+1) : fy = fy*y%self.mod
        for xy in range(1,X+Y+1) : fxy = fxy*xy%self.mod
        deno = pow(fx*fy%self.mod,self.mod-2,self.mod)
        return fxy*deno%self.mod

class MOD:
    def __init__(self,mod,N=4000001):
        self.mod = mod
        self.fac = [0]*N
        self.finv = [0]*N
        self.inv = [0]*N
        self.fac[0] = self.fac[1] = self.finv[0] = self.finv[1] = self.inv[1] = 1
        for i in range(2,N):
            self.fac[i] = self.fac[i-1]*i%mod
            self.inv[i] = mod-self.inv[mod%i]*(mod//i)%mod
            self.finv[i] = self.finv[i-1]*self.inv[i]%mod
    def modC(self,X,Y):
        return self.fac[X+Y]*self.finv[X]%self.mod*self.finv[Y]%self.mod
