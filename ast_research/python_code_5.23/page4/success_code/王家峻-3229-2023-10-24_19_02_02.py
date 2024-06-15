n=eval(input())
from collections import Counter
c=Counter(n)
b=[t for t,count in c.items() if count==1]
b.sort()
h=list(map(int,b .spilt(',')))
print(h)
