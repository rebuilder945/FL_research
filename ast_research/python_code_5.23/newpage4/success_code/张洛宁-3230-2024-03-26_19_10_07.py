scores=eval(input())
scores.sort(reverse=True)
m=scores
f=sum(m)
if f==0:
    print("0")
else:
    s=""
    for x in m:
        s=s+str(x)+""
    print(s)









