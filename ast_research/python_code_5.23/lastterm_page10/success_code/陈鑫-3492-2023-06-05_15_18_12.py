a=input()
b={}
for i in a:
    b[i]=b.get(i,0)+1

for x in list(b.keys()):
    if b[x]==1:
        print(x)
        break
else:
    print('None')


