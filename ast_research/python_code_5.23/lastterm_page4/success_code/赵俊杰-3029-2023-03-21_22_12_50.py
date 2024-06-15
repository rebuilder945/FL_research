ls1=eval(input())
ls1=list(ls1)
ls2=eval(input())
a=len(ls1)
list=[ls1[x]+","+ls2[x] for x in range(0,a)]
print(list)
