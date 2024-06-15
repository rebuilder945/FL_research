ls=eval(input())
ls=list(ls)
ls.reverse()
ls2=[]
for x in ls:
    if x not in ls2:
        ls2.append(x)
ls2.reverse()
print(ls2)    

