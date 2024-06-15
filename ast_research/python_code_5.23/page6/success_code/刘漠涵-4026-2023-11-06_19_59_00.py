n=int(input())
lst=[1,2]
lst0=[]
while len(lst)<n+1:
    a=int(lst[-1])
    b=int(lst[-2])
    k=a+b
    lst.append(k)
j=1
while j<=len(lst)-1:
    a=int(lst[j])/int(lst[j-1])
    lst0.append(a)
    j+=1
c=sum(lst0)
print('%.4f'%c)
