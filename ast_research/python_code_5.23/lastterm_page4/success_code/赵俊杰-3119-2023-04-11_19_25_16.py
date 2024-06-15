ls=eval(input())
ls2=[]
for x in ls[::-1]:
    if x not in ls2:
        ls2.append(x)
    else:
        pass
ls2.reverse()
print(ls2)
