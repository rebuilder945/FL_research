a=list(input())
b=[int(x) for x in a]
lst=[]
for i in b:
    i=(i+5)%10
    lst.append(i)

sum=0
for x in range(len(lst)):
    d=lst[x]*10**x
    sum+=d
print(sum)
