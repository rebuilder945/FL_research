list1=eval(input())
list1=list(list1)
n,m=eval(input())
if n >=len(list1):
    print("error")
else:
    x1=list1[n]
    while m>0:
        list1.append(int(x1))
        m-=1
    print(list1)
