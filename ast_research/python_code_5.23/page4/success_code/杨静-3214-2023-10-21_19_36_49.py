ls=eval(input())
ls1=[]
while 0 in ls:
    ls.remove(0)
    ls1.append(0)
ls.extend(ls1)
print(ls)
