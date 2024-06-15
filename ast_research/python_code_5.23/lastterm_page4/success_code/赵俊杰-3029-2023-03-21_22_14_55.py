ls1=list(input())
ls2=eval(input())
a=len(ls1)
ls3=[ls1[x]+","+ls2[x] for x in range(0,a)]
print(ls3)
