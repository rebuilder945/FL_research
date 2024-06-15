from re import M


scores=eval(input())
scores.sort(reverse=True)
m=scores
f=sum(m)
print(f)
if f==0:
    print(f)
else:
    s=""
    for x in m:
        s=s+str(x)+""
    print(s)
    








