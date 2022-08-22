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
  
