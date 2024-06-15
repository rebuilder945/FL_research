shu=eval(input())
ls=[]
for x in shu:
    if x!=0:
        ls.append(x)
b=shu.count(0)
for i in range(b):
    ls+=[0]
print(ls)
