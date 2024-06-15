l = input().split()
n,m = eval(input())
if l[n]==True:
    for i in range(m):
        l.append(l[n])
        print(l)
if l[n]==False:
    print("error")
