s=input()
lst=list(s.split())
strcount={}
for i in lst:
    strcount[i]=lst.count(i)
lst2=[]
for j,k in strcount.items():
    lst2.append([j,k])
lst2.sort(key=lambda x:x[1],reverse=True)
a=1
for i in range(len(lst2)-1):
    if lst2[i][1]==lst2[i+1][1]:
        a=a+1
l3=[]
for i in range(a):
    x,y=lst2[i][0],lst2[i][1]
    l3.append([x,y])
    l3.sort(key=lambda x:x[0],reverse=False)
l4=tuple(l3)
print(*l4,sep=' \n')
