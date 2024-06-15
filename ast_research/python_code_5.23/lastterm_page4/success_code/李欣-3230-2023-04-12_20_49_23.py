lst=eval(input())
lst1=sorted(lst)
a=int(len(lst))
s=0
for x in range(a):
    m=int(lst1[x])*10**x
    s+=m
print(s)
