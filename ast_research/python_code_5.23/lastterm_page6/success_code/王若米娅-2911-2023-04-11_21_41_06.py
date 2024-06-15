
lst=list(map(input().split('')))
n=len(lst)
lst[0]=lst[n-1]
lst[1]=lst[n-2]
lst1=[]
for x in lst:
    c=(x+5)%10
    lst1.append(c)
print(*lst1,sep='')
