ls1 = list(input())
n,m = eval(input(""))
if n in (0,len(ls1)):
    ls2 = ls1[n-1]*m
    ls1 = ls1+ls2
    print(ls1)
else:
    print("error")
