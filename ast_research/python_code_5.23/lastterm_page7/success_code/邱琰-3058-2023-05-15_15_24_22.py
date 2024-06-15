n=input()
lst=[]
while n!='q':
    lst.append(n)
d={}
for i in lst:
    if i not in d:
        d[i]=1
    if i in d:
        d[i]+=1
a=max(d)
print(a)



