lll=input().split(' ')
n,m=input().split()
lst=[]
c=lll[int(n)]
d=lll[int(m)]
for i in range(len(lll)):
    lst.append(lll[i])
lst[m]=c
lst[n]=d
print(lst)
