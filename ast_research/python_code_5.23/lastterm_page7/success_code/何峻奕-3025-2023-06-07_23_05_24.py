s=list(input().split())
a=[]
s.sort()
for i in s:
    d=s.count(i)
    if d not in a:
        a.append(d)
for x in s:
    if s.count(x)==max(a):
        print(x,max(a))
        
