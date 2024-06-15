lst=input().split()
d={}
for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
num=list(d.items())
num.sort(key=lambda x:x[1],reverse=True)
n=num[0][1]
num.sort()
for x in num:
    if x[1]==n:
        a,b=x
        print("{} {}".format(a,b))

