ls1=list(eval(input()))
n,m=eval(input())
ls2=ls1.copy()
if n>=len(ls1) or ((-1)*n)>len(ls1):
     print("error")
else:
    for i in range(m):
        ls1.append(ls2[n])
    print(ls1)
