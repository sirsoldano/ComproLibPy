# tc : NloglogN
# ul : 10^7
def erast(N):
	prime,is_prime,p = [],[0,0]+[1]*(N-1),2
	while p<=N:
		if is_prime[p]:
			prime.append(p)
			for i in range(2,N//p+1)
				is_prime[i*p]=0
		p+=1
	return prime

# tc : √N
# ul : 10^12
def tridiv(n):
	pf = []
	f = 2
	while f*f<=n:
		if n%f == 0 :
			pf.append(f)
			n//=f
		else:
			f = f+2 if f>2 else 3
	if n>1:
		pf.append(n)
	return pf
# 複数回実行する場合は事前に素数列挙
# PL=erast(int(n**0.5))
def tridivPL(n,PL):
	pf = []
	ind=0
	while ind<len(PL) and PL[ind]*PL[ind]<=n:
		if n%PL[ind] == 0 :
			pf.append(PL[ind])
			n//=PL[ind]
		else:
			ind+=1
	if n>1:
		pf.append(n)
	return pf


import collections
collections.Counter(tridiv(int(input())))

#GCD
# tc : log(A+B)
# ul : over 10^18
def gcd(A,B):
	while A>=1 and B>=1 :
		if(A>B):
			A = A%B
		else:
			B = B%A
	return A if A else B
# use library
import math
math.gcd(A,B)
lcm = A*B//math.gcd(A,B)
