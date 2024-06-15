lst = [int(x) for x in input().split(',')]
n,m = map(int,input().split(','))
pos = 0
if n >= len(lst):
    print("error")
else:
    notic = lst[n]
    lst += [notic] * m
    print(lst)


