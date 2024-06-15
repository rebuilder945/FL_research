ls=eval(input())
n,m=eval(input())
a=len(ls)
ls1=[]
ls2=[]
if n>=a or n<-a:
    print("error")
else:
    ls1.append(ls[n])
    ls2=(ls1*m)
    ls.append(ls2)
    print(ls)
