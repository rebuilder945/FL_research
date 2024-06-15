m = eval(input())
a, b = input().split(',')
n = int(a)
p = int(b)
if p > len(m):
    print("error")
else:
    del m[n:m]
    print(m)


    












