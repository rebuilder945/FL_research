a=input()
d={}
while a !='q':
    if a in d:
        d[a]+=1
    else:
        d[a]=1
    a=input()
b=0
for i in d.values():
    if i>b:
        b=i
    else:
        b=1
for j in d.keys():
    if d[j]==b:
        print("{} {}".format(j,b))
