a = input().split(',')
n,m = eval(input())
lst = list(a)
if n>=0 and n<=len(lst):
    for i in range(m):
        lst.append(lst[n])
    lst1 = list(map(int,lst))
    print(lst1)
elif n<0 and abs(n)<=len(lst):
    f = len(lst)+n+1
    for x in range(m):
        lst.append(lst[f])
    lst1 = list(map(int,lst))
    print(lst1)
else:
    print("error")
