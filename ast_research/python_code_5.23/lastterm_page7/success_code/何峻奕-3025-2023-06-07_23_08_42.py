s=list(input().split())
a=[]
b=[]
s.sort()
for i in s:
    d=s.count(i)
    a.append(d)
for x in s:
    if x not in b:
        b.append(x)
        if s.count(x)==max(a):
            print(x,max(a))
        
