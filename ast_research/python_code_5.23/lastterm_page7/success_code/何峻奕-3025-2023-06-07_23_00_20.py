s=list(input().split())
a=[]
s=s.sort()
for i in s:
    d=s.count(i)
    a.append(d)
for x in s:
    if s.count(x)==max(a):
        print(x,max(a))
        continue
