lst=[]
i=input()
while i!="q":
    lst.append(i)
    i=input()
n=0
mmax=0
a=0
n1=0
for m in lst:
    n=lst.count(m)
    if n>n1:
        mmax=n
        a=m
    n1=n
print(a,mmax)


