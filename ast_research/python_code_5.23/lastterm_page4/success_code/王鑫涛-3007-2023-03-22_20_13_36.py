a = list(eval(input()))
n,m=eval(input())
if m >(len(a)-1):
 print("error")
else:
    for i in range(m-n):
        del a[n]
    print(a)
