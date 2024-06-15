n=eval(input())
d=[i for i in range(1,n+1)]
e=[]
for i in d[1: ]:
    e.append(i)
e.append(d[0])
print(e)

