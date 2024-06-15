lst=list(input().split(","))
num=eval(input())
n=num[0]
m=num[1]
N=lst[n]
if n >= len(lst):
    print("error")
else:
    for i in range(m):
        lst.append(N)
    lst=str(lst).replace("'","")
    print(lst)
