n=eval(input())
from collections import Counter
c=Counter(n)
t=[i for i in c if c[i]==1]
if t :
    t.sort()
    print(t)
else:
    print(False)
  
