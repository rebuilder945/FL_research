lst = list(map(int,input().split(',')))
n,m = eval(input())
if n+1 > len(lst):
    print('error')
else :
    for x in range(m):
        lst.append(lst[n])
    print(lst)

