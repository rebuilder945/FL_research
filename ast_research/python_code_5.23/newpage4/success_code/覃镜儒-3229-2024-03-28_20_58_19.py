i=eval(input())
from collections import Counter
n=Counter(i)
a=[elem for elem,count in n.items()if count==1]
if not a:
    print(False)
else:
    b=sort(a)
    for elem in b:
        print(elem,end=",")
