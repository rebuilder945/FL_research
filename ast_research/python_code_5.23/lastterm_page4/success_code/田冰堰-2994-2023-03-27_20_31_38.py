ls=eval(input())
n,m=eval(input())
a=len(ls)
ls1=[]
if n>=a:
    print("error")
else:
    ls1.append(ls[n])
    print(ls+ls1*m)
