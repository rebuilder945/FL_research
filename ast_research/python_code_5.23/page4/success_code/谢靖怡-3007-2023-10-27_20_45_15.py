lst=input()
n,m=input().split(",")
if n in (0,len(lst)) and m in (0,len(lst)) and n < m:
    del lst[n:m]
    print(list(lst))
else:
    print("error")
