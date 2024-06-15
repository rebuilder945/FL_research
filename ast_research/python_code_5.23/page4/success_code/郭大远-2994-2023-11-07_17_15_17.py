list1=eval(input())
list2=list(list1)
list3=list2.copy()
n,m=eval(input())
if 0<=n<=len(list2):
    for i in range(m):
        b=list2[n]
        list3.append(b)
    print(list3)
elif   -len(list2)<=n<=-1:
    for i in range(m):
        b=list2[n]
        list3.append(b)
    print(list3)
else:
    print("error")


