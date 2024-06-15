a = list(eval(input()))
n,m=eval(input())
if m >(len(a)-1) or n<0:
 print("error")
else:
    for i in range(m-n):
        del a[n]
    print(a)
