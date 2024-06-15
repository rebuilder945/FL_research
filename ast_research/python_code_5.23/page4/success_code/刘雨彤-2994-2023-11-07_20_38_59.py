a=list(eval(input()))
n,m=eval(input())
if n >=len(a):
    print("error")
else:
     x1=a[n]
     while m>0:
        a.append(int(x1))
        m-=1
print(a)






