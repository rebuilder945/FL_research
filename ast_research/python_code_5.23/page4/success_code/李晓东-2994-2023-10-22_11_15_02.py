a = list(map(int,input().split(",")))
n,m = eval(input())
b = a[n]
d = []
if n >=len(a) :
    print("error")
else:
    for i in range(m):
        d.append(b)
a = a+d
print(a)
