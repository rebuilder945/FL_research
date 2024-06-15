l = input().split()
n,m = eval(input())
if l[n]==False:
    print("error")
else:
    for i in range(m):
        l.append(l[n])
        print(l)
