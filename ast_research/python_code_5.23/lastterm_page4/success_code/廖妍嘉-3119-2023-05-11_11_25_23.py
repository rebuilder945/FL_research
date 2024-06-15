ls=eval(input())
ls2=[]
ls.reverse()
for i in ls:
    if i not in ls2:
        ls2.append(i)
ls2.reverse()
print(ls2)
