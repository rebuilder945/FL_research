ls1=eval(input())
ls1.sort(reverse=True)
#print(ls1)
if ls1[0]==0 : print(0)
else:
    for i in ls1:
        print(i,end='')
