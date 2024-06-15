i=eval(input())
from collections import Counter
n=Counter(i)
a=[elem for elem,count in n.items()if count==1]
if not a:
    print(False)
else:
    b=sorted(a)
    for elem in b:
        if len>1:
            print(elem,end=",")
        else:
            print(elem)
