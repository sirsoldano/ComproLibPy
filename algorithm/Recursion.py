# 分割統治法
def DivCon(l,r) :
	if r-l==1 :
		return A[l]
	m = (l+r)//2
	return divcon(l,m)+divcon(m,r)

# マージソート
# tc : NlogN
# ul : 10^6
def MergeSort(l,r) :
	if r-l==1 :
		return
	m = (l+r)//2
	MergeSort(l,m); MergeSort(m,r)
	ordered,c1,c2,cnt = [0]*(r-l),l,m,0
	while c1<m or c2<r :
		if c1==m or ( c2<r and A[c2]<=A[c1] ):
			ordered[cnt] = A[c2]
			c2+=1
		else:
			ordered[cnt] = A[c1]
			c1+=1
		cnt+=1
	for c in range(cnt):
		A[l+c]=ordered[c]
