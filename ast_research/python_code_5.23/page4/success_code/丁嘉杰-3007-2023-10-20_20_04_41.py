ls1=eval(input())
ls2=input().split(",")
n=eval(ls2[0])
m=eval(ls2[1])
if n>m:
    print("error")
else:
    del(ls1[n:m])
    print(ls1)
