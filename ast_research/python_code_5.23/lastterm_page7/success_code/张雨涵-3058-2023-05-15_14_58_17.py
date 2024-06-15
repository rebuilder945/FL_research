str = input()
a=[]
b={}
while str!="q":
    a.append(str)
    str = input()
for i in a:
    t =a.count(i)
    b.setdefault(i,t)
for c,d in b.items():
    if d == max(b.values()):
        print(c,d)
