a=input()or''
b={}
for i in a:
    b[i]=b.get(i,0)+1
for x in b:
    if b[x]==0:
        print(x)
        break
    else:
        print('None')


