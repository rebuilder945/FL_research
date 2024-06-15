a=list(eval(input()))
n,m=eval(input())
ls=[]
flag=1
if n<=len(a):
    for i in range(m):
        ls.append(a[n])
        flag=0
if flag==0:
    print(a+ls)
else:
    print("error")




