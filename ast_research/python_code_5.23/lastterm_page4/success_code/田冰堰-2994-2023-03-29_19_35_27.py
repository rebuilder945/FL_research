ls=eval(input())
n,m=eval(input())
a=len(ls)
ls1=[]
ls2=[]
if n>=a or n<0:
    print("error")
else:
    ls1.append(ls[n])
    ls2=(ls1*m)
    print(ls2)
