grid = [0]*(H*W)
# 隣接するマスの判定
pos = (h-1)*W + w-1
if pos-W>=0 and mp[pos-W] : 
if (pos+1)%W!=0 and mp[pos+1] : 
if pos+W<H*W and mp[pos+W] : 
if pos%W!=0 and mp[pos-1] : 
