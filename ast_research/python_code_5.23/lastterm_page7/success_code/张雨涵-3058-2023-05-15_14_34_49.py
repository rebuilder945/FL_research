str = input()
a=[]
b=[]
while str!="q":
    a.append(str)
    str = input()
for i in a:
    t =a.count(i)
    b.append(t)
print(max(b))
