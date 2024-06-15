ls=eval(input())
x=''
y=[]
for i in ls:
    x+=i
x=list(x)
for j in x:
    if j not in y:
        y.append(j)
y.sort()
for a in y:
    print(str(a)+','+str(x.count(a)))

