list_1 =list(eval(input()))
n,m=eval(input())
if -len(list_1)<=n<=len(list_1)-1:
    for i in range(m):
        list_1.append(list_1[n])
    print(list_1)
else:
    print("error")

