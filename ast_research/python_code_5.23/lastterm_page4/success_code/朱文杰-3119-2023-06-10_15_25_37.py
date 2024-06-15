ls=eval(input())
ls2=[]
for i in ls[::-1]:
    if i not in ls2:
        ls2.insert(0,i)
print(ls2)
