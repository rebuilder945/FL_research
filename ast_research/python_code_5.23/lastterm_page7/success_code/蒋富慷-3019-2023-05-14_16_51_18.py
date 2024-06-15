l = input().split( )
a,b,c,d=l
stu = {}
e = {}
h = []
stu["name"] = a
stu["english"] = '%.2f'%(b)
stu["python"] = '%.2f'%(c)
stu["math"] = '%.2f'%(d)
m = int(b+c+d)/3
stu["avg"] = '%.2f'%(m)
e["english"] = b
e["python"] = c
e["math"] = d
for f,g in e.items():
    h.append([f,g])
h.sort(key=lambda x:x[1],reverse=True)
i = h[0][0]
j = h[1][0]
k = h[2][0]
print(stu["name"],stu[i],stu[j],stu[k],stu["avg"],)
