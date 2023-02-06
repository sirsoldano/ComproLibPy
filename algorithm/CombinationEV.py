# fast combination
# ul : 100
for a in range(N-4):
    for b in range(a+1,N-3):
        for c in range(b+1,N-2):
            for d in range(c+1,N-1):
                for e in range(d+1,N):

# 少ないパターンの側に着目し数え上げる
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_v

# 全出現までの回数期待値 r枚出現時 : (r/N)^0+(r/N)^1+(r/N)^2+(r/N)^3+... = N/(N-r)
# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_z

# 各桁の数字の和＝Kの通り数
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/042.jpg
dp = [1]+[0]*K
for k in range(1,K+1):
    for i in range(1,min(k,9)+1):
        dp[k]+=dp[k-i]
        dp[k]%=1000000007

# 包除原理（余事象の合成）https://github.com/E869120/kyopro_educational_90/blob/main/editorial/080.jpg
ans = 2**D
for i in range(1,2**N):
    con = 0
    temp = 0
    for n in range(N):
        if 2**n & i :
            temp|=a[n]
            con+=1
    free = 0
    for d in range(D):
        if 2**d&temp==0:
            free+=1
    if con%2==1 : ans-=2**free
    else : ans+=2**free
