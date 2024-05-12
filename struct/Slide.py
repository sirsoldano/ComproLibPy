# スライド最小値
from collections import deque
def slide_max_index(a, K):
    # max_idx[i]: 区間 [i - K + 1, i] (両側閉区間)における a の最大値を与えるインデックス
    N = len(a)
    max_idx = [0] * N # (長さKに満たない左側領域もついでに計算する)
    deq = deque() # デック．番長順番待ちキューをシミュレートする．インデックスを格納しておく
    for i in range(0,N):
        while len(deq) > 0 and deq[0] <= i - K : deq.popleft() # 卒業する
        while len(deq) > 0 and a[deq[-1]] < a[i] : deq.pop()   # a[i] の入学で 望みがなくなった先輩達が脱落する
        deq.append(i)                                          # 新入生i は常に番長になる望みがある
        max_idx[i] = deq[0]                                    # 番長順番待ちキューの最左が番長

    return max_idx

# ヒストグラム内長方形
def first_exceeder(a):
    # exceeder[i]: iより右側で a[i]を最初に超えるaのインデックス
    N = len(a)
    exceeder = [0] * N
    stk = [] #番長順番待ちキュー
    for i in range(0,N):
        # iが入学
        while len(stk) > 0:
            righttail = stk[-1]
            if a[righttail] < a[i]:
                exceeder[righttail] = i #順番待ちキューのセンパイが自分より弱い場合，センパイに自分の名前を告げて引導を渡す
                stk.pop()               #センパイがキューから離れる
                continue
            break
        stk.append(i)  # 自分がキューに並ぶ
    # 自分より強い後輩が入ってこなかったメンバーはキューに残ったままなので右端をexceederにする
    for i in stk:
        exceeder[i] = N
    return exceeder
＃ ABC353
stk = [(0,N)]
ans = 0
for n in range(N-1):
  bn = n
  while a[n] < stk[-1][0]:
    h,bn = stk.pop()
    ans += ((n-bn+1)*(n-bn)//2)*(h-max(a[n],stk[-1][0]))
  if stk[-1][0]<a[n]:
    stk.append((a[n],bn))
while len(stk)>1 :
  h,bn = stk.pop()
  ans += ((N-bn)*(N-bn-1)//2)*(h-stk[-1][0])
print(ans)
