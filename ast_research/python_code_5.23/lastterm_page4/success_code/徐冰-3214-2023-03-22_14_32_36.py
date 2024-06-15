ls1=eval(input())
ls2=[]
while 0 in ls1:
    ls1.remove(0)
    ls2.append(0)
ls1.extend(ls2)
print(ls1)
