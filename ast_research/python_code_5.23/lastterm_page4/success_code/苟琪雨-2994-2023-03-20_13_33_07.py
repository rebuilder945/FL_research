list1=list(eval(input()))
n,m=map(int,input().split(','))
if n<len(list1):
    a=list1[n]
    for i in range(m):
        list1.append(a)
    print(list1)
else:
    print("error")
