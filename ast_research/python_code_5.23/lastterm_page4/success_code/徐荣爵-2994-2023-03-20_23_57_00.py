lst = list(map(int,input().split(',')))
n,m = eval(input())
if n+1 > len(lst):
    print('error')
else :
    t = lst[n:n+1]
    t = t[0]
    for x in range(m):
        lst.append(t)
    print(lst)

