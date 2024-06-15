list_1 =list(eval(input()))
n,m=eval(input())
a=list_1[n]
if -len(list_1)<=n<=len(list_1)-1:
    for i in range(m):
        list_1.append(a)
    print(list_1)
else:
    print("error")

