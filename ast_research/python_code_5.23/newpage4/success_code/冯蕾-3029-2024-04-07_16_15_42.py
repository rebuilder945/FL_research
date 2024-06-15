n=input().split(',')
s=input().split(',')
s2=[]
for i in s:
    i=eval(i)
    s2.append(i)

m=len(s)
lst1=[]
lst=zip(n,s2)
for i in lst:
    lst1.append(list(i))
lst1.sort(key=lambda x:x[1])
print(lst1)
