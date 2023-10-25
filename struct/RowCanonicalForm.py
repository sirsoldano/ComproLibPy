# 行基本変形
D = len(format(max(a),"b"))
import heapq as hq
q,rcf = [],[]
for n in range(N) : hq.heappush(q,-a[n])
for d in range(D,-1,-1):
  if q and -q[0]>=2**d:
    bit = -hq.heappop(q)
    for i in range(len(rcf)):
      if (rcf[i]>>d)&1 :
        rcf[i] ^= bit
    rcf.append(bit)
    while q and -q[0]>=2**d:
        i = -hq.heappop(q)
        i ^= bit
        hq.heappush(q,-i)
