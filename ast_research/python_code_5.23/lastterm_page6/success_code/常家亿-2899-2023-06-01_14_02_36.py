n,m = map(int,input().split())#空格隔开输入
lst = []
if 0<=n<m and m-n>=3:
    for x in range(n,m):
        lst.append(x)
else:
    print('illegal input')
lst1 =[] 
from itertools import permutations
for p in permutations(lst,3):
    if p[0] != 0:
        q = ''.join(str(s) for s in p)
        lst1.append(q)
print(' '.join(str(i) for i in lst1))   








