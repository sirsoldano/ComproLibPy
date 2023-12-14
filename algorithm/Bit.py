# 最小TrueBit桁
mindig = i & -i

# mod2の掃き出し法(複数回のXOR) https://atcoder.jp/contests/typical90/tasks/typical90_be (解説:https://github.com/E869120/kyopro_educational_90/blob/main/editorial/057.jpg)
A,S = [0]*N, 0
for n in range(N):
    for m in map(lambda x:int(x)-1,input().split()) : A[n] += 1<<m
for m,b in enumerate(map(int,input().split())) : 
    if b : S += 1<<m
pos = 0
for m in range(M):
    found = False
    for n in range(pos,N):
        if A[n]&(1<<m) :
            if n!=pos : A[n],A[pos]=A[pos],A[n]
            found = True
            break
    if found:
        for n in range(N):
            if n!=pos and A[n]&(1<<m) : A[n] ^= A[pos]
        if S&(1<<m) : S ^= A[pos]
        pos+=1

# dpの64倍高速化
xy = sorted([list(map(lambda x:int(x)-1,input().split())) for m in range(M)],key=lambda x:(x[1],x[0]))
ab = [tuple(map(lambda x:int(x)-1,input().split())) for q in range(Q)]
for q in range(0,Q,50):
    dp = [0]*N
    for i in range(q,min(Q,q+50)) : dp[ab[i][0]] += 1<<(i-q)
    for m in xy : dp[m[1]] |= dp[m[0]]
    for i in range(q,min(Q,q+50)): print("Yes") if dp[ab[i][1]]&1<<(i-q) else print("No")

# 部分集合列挙 tc:3^N
bit=[[i] for i in range(1<<N)]
for i in range(1<<N):
    subbit = i
    while subbit>0:
        subbit = (subbit-1) & i
        bit[i].append(subbit)
