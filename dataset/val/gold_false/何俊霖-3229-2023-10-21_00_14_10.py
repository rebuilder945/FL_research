x=eval(input())
y=[]
t=0
for i in range(0,len(x)):
    c=x.count(x[i])
    t+=c
    if c==1:
        if x[i] not in y:
            y.append(x[i])
if y==[]:
    print("False")
else:
    y.sort(reverse=False)
    s=""
    for r in range(0,len(y)):
        s=s+str(y[r])+","
    s=s[-2::-1]
    print(s)


