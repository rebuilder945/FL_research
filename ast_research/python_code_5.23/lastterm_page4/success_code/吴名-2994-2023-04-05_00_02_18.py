lst=list(input().split(","))
num=eval(input())
n=num[0]+1
m=num[1]
if n >= len(lst):
    print("error")
else:
    for i in range(m):
        lst.append(n)
    print(lst)
