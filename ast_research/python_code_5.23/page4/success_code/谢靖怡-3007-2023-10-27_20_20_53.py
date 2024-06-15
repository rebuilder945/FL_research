lst=input()
n,m=eval(input().split(","))
if n in (0,len(lst)-1) and m in (0,len(lst)-1):
    for i in range(lst[0:]):
        if i>lst[n] and i<lst[m]:
            del lst[n:m]
        else:
            continue
    print(lst)
else:
    print("error")
