ls=eval(input())
ls1=[]
n,m=eval(input())
for x in ls:
    ls1.append(x)
if n>=len(ls1) or n<-len(ls1):
    print("error")
else:
    for i in range(m):
        ls1.append(ls1[n])
    print(ls1)
