a = list(eval(input()))
n,m=eval(input())
if m<(len(a)-1):
    for i in range(m-n):
        del a[n]
    print(a)
else:
    print("error")

