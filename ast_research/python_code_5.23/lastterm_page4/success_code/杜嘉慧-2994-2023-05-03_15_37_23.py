lst = [int(x) for x in input().split(',')]
n,m = [int(x) for x in input().split(',')]
pos = 0
if n >= len(lst):
    print("error")
else:
    notic = lst[n]
    lst += [notic] * m
    print(lst)



