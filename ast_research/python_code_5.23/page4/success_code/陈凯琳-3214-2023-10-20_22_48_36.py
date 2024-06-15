ls=eval(input())
ls2=[]
for i in range(len(ls)):
    if 0 in ls:
        ls.remove(0)
        ls2.append(0)
print(ls+ls2)
