ls=input()[1:-1].split(",")
ls=[eval(i)for i in ls]
ss=input("").split(",")
n,m=eval(ss[0]),eval(ss[1])
if n>len(ls)or m>len(ls)
    print("error")
    return
elif n<m:
    ls=ls[:m+1]+ls[n+1]
print(ls)
