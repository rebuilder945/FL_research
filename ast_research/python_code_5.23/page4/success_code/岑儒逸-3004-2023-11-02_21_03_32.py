

ls=eval(input())
D=[]
for i in ls:
    yinshu=[]
    for x in range(1,i):
        if i % x==0:
            yinshu.append(x)
    if len(yinshu)==1:
        D.append(i)
print(D)
