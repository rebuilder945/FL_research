
from itertools import count


a=input() or "p"
count={}
while(a!="p"):
    count[a]=count.get(a,0)+1
countlist=list(count.items())
countlist.sort(key=lambda x:x[1].reverse=True)
print(countlist.countlist[0])
