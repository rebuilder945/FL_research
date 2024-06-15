a=int(input())
b=[]
for x in range(100,1000):
    if x==int(str(x)[0])**3+int(str(x)[1])**3+int(str(x)[2])**3:
        b.append(x)
c=[]
for x in b:
    if x<=a:
        c.append(x)
if c==[]:
    print('none')
else:
    for x in c:
        print(x)

