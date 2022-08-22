# tc : √N
# ul time : 10^12
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

import collections
collections.Counter(tridiv(int(input())))
