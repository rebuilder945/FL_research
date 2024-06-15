lst=[]
i=input()
while i!="q":
    lst.append(i)
    i=input
count=0
count1=0
for x in lst:
    for m in lst:
        if m==x:
            count+=1
        if count1<count:
            mmax=count
            n=x
        count1=count
print(n,mmax)
