ls1=eval(input())
ls2=[]
for a in ls1:
    for i in range(2,a):
        if not a%i==0:
            ls2.append(a)
            break
if 2 not in ls1:
    print(ls2)
else:
    ls2.append("2")
    print(ls2)
