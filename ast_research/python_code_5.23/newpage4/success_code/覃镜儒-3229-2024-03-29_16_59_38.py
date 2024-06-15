i=eval(input())
from collections import Counter
n=Counter(i)
a=[elem for elem,count in n.items()if count==1]
if not a:
    print(False)
else:
    b=sorted(a)
    for index,elem in enumerate(b):
        if index<len(b)-1:
            print(elem,end=",")
        else:
            print(elem)
