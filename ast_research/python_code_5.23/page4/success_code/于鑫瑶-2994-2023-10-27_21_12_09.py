ls1=eval(input())
ls1=list
n,m=map(int,(input().split(",")))
ls2=[]
if n>len(ls1):
    ls2.append(ls1[n])
    ls2*m
    ls1.extend(ls2)
    print(ls1)
else:
    print("error")
