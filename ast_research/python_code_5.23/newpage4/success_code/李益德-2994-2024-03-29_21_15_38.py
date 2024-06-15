list_1 =list(eval(input()))
n,m=eval(input())

if -len(list_1)<=n<=len(list_1)-1:
    a=list_1[n]
    for i in range(m):
        list_1.append(a)
    print(list_1)
else:
    print("error")

