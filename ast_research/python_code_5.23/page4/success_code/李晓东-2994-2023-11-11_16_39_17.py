a = list(map(int,input().split(",")))
n,m = eval(input())
b = len(a)
if n>=b or -n>b:
    print("error")
else:
    list1 = []
    c = a[n]
    for i in range(m):
        list1.append(c)
    print(a+list1)


