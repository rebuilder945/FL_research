list1 = list(map(int,input().split(",")))
n,m = map(int,input().split(","))
a = len(list1)
if n<=a-1 or -n<=a:
    b = list1[n]
    for i in range(m):
        list1.append(b)
    print(list1)
else:
    print("error")
