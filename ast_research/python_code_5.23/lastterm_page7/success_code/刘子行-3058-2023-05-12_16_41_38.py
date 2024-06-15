a=input() or "q"
a1={}
i=0
while(a!="q"):
    a1[i]=a
    i+=1
    a=input() or "q"
ls1=list(a1.values())
num=[]
for x in ls1:
    num.append(ls1.count(x))
big=max(num)
alpha=''
for x in ls1:
    if ls1.count(x)==big:
        alpha=x
print(alpha,big)
