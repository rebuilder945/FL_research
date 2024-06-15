lst=input().split(',')
n,m=input().split(',')
n=int(n)
m=int(m)
if n<len(lst):
    a=lst[n]
    for x in range(m):
        lst.append(a)
    lst=list(map(int,lst))
    print(lst)
else:
    print("error")
