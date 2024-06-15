list1=list(eval(input()))
n,m=eval(input())
if n>=len(list1):
    print("error")
else:
    x=list1[n]
    while m>0:
        list1.append(x)
        m-=1
    print(list1)

