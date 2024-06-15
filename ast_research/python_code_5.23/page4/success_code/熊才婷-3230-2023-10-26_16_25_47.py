lst=eval(input())
lst.sort(reverse=True)
m=len(lst)-1
sum=0
lst1=[]
for i in lst:
    lst1.append(i)
for i in lst1:
    a=i*(10**m)
    sum+=a
    m-=1
print(int(sum))
