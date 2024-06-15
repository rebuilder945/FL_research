list=eval(input())
a=[]
for i in list[:]:
    for x in range(2,i):
        if i%x==0:
            pass
        else:
            a.append(i)
print(a)

