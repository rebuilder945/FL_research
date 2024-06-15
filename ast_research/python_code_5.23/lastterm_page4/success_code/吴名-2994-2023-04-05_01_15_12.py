lst=list(input().split(","))
num=eval(input())
n=num[0]
m=num[1]
if (n+0.5)**2 >= (len(lst))**2:
    print("error")
else:
    N=lst[n]
    for i in range(m):
        lst.append(N)
    lst=str(lst).replace("'","")
    print(lst)
