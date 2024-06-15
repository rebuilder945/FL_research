lst=eval(input())
n,m=eval(input())
lenth=[x for x in range(len(lst))]
if m in lenth and n in lenth:
    del lst[n:m]
    print(lst)
else:
    print(error)
