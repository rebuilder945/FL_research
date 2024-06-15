a = list(eval(input()))
n,m = eval(input())
b = []
if n>0 and n<len(a):
    for i in range(m):
        b.append(a[n])
    print(a+b)
elif n<0 and -n<=len(a):
    for i in range(m):
        b.append(a[n])
    print(a+b)
else:
    print("error")

