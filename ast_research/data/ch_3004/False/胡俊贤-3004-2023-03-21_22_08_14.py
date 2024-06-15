ls=eval(input())
a=[]
for i in ls:
    for t in range(2,i//2+1):
        if i % t==0:
            a.append(i)
print(a)

