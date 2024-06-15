ls1 = list(input())
n,m = eval(input())
if n >=0 and n <=len(ls1):
    ls2 = list(ls1[n-1]*m)
    ls3 = ls1.extend(ls2)
    print(ls3)
else:
    print("error")
    
