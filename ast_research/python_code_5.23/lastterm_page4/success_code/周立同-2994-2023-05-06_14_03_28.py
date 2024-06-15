lst=input().split(",")
lst2=list(map(int,lst))
n,m=eval(input())
if -len(lst)<n<len(lst)-1:
    a=lst2[n]
    for i in range(0,m):
        lst2.append(a)
    print(lst2)
else:
    print("error")

