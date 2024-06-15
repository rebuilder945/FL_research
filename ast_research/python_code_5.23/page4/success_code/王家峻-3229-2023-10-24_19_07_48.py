n=eval(input())
from collections import Counter
c=Counter(n)
for i in c:
    while i >1:
        print(i.spilt(','))
    else:
        print(False)
