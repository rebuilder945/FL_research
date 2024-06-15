list1=eval(input())
n,m=eval(input())
if 0<n<len(list1):
    a=list1[n-1]
    for x in range(m):
        list1.append(a)
    print(list1)
elif -len(list1)<n<0:
    b=list1[n]
    for x in range(m):
        list1.append(b)
    print(list1)
else:
    print('error')
