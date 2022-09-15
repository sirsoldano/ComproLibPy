# 辞書順最小→前から貪欲法(残り文字数を満たす中で一番若い文字をセレクトしansに追加) (https://atcoder.jp/contests/typical90/tasks/typical90_f)
# その文字の次の出現場所を事前に計算し保存
S = list(map(lambda x:ord(x)-97,input().rstrip()))
ncpos = [[-1]*26 for c in range(N+1)]
for n in range(1,N+1):
    for c in range(26):
        if c == S[-n] : ncpos[N-n][c]=N-n
        else : ncpos[N-n][c]=ncpos[N-n+1][c]
ans,n=[],0
while n<N and len(ans)<K:
    for j in range(26):
        if N-ncpos[n][j]>=K-len(ans) and ncpos[n][j]>=0:
            ans.append(j)
            n=ncpos[n][j]+1
            break
