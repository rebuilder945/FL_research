lll=input().split('')
n,m=input().split('')
lst=[]
c=lll[n]
d=lll[m]
for i in range(len(lll)):
    lst.append(lll[i])
lst[m]=c
lst[n]=d
print(lst)
