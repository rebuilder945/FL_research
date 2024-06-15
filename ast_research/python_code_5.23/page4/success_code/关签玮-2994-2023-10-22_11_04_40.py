ls1=eval(input())
a,b=eval(input())
ls2=[]
if len(ls1)>a>=-len(ls1):
    ls2=[ls1[a]]*b
    print(list(ls1)+ls2)
else:print("error")
