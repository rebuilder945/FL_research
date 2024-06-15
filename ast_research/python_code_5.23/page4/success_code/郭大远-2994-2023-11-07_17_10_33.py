list1=eval(input())
list2=list(list1)
n,m=eval(input())
if 0<=n<=len(list2):
    for i in range(m):
        b=list2[n]
        list2.append(b)
    print(list2)
elif   -len(list2)<=n<=-1:
    for i in range(m):
        b=list2[n]
        list1.append(b)
    print(list2)
else:
    print("error")


