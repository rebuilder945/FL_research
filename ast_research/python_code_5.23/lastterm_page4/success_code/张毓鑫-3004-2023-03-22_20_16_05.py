a=eval(input())
b=[]
c=[]
for i in a:
    b.append(i)
for i in a:
    for x in range(2,i):
        if i%x==0:
            b.remove(i)

print(b)
