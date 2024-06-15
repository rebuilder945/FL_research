a = input().split=","
b,c = eval(input())
if b >= len(a):
    print("error")
else:
    for i in range(c):
        a.append(a[b])
    print(a)
