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

# 経時タスクの取捨選択は締め切り(終了時間)でソート https://atcoder.jp/contests/typical90/tasks/typical90_k
# dp[タスク順][タイムポイント]でタスクの可否で場合分け
DCS = sorted([tuple(map(int,input().split())) for n in range(N)]) # D:締め切り, C:所要時間, S:報酬
dp = [[0]*5001 for n in range(N+1)]
for n in range(1,N+1):
    for t in range(5001):
        if DCS[n-1][1]<=t<=DCS[n-1][0] : dp[n][t] = max(dp[n-1][t],dp[n-1][t-DCS[n-1][1]]+DCS[n-1][2])
        else : dp[n][t] = dp[n-1][t]
