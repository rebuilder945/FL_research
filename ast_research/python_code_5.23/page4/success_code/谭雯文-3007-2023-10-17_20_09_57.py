lst1=input().split(",")
n,m=eval(input())
if n<=(len(lst1)-1) and m<=(len(lst1)-1):
    for i in range(n,m):
        print(lst1.pop(i))
else:
    print("error")


