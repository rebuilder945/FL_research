ls1=eval(input())
ls2=[]
for a in ls1:
    for i in range(2,a):
        if  a%i==0:
            ls1.remove(a)
            break
print(ls1)
