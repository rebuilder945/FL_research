a=list(eval(input()))
v=len(a)
n,m=eval(input())
if n<=v-1:
    f=[a[n]]
    h=a+f*3
    print(h)
else:
    print("error")

