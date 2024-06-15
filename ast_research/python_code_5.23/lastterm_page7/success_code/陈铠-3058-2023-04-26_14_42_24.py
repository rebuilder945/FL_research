lst=[]
d={}
while True:
    a=input()
    if a =='q':
        break
    else:
        lst.append(a)
for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
num=list(d.items())
num.sort(key=lambda x:x[1],reverse=True)
m,n=num[0]
print("{} {}".format(m,n))
