ls1=eval(list(input()))
n,m=eval(input())
ls2=[]
if n in len(ls1):
    ls2.append(ls1[n])
    ls2*m
    ls1.extend(ls2)
    print(ls1)
else:
    print("error")
