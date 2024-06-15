lst=eval(input())
num=[]
for x in lst:
    if lst.count(x)==1:
        num.append(x)
num.sort()
if len(num)==0:
    print(False)
else:
    a=",".join([str(i) for i in num])
    print(a)

