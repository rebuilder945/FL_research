from itertools import count


x=eval(input())
y=[]
t=0
for i in range(0,len(x)):
    c=x.count(x[i])
    t+=c
    if c==1:
        if x[i] not in y:
            y.append(x[i])
y.sort(reverse=True)

