lst = input().split(',')
n,m = [int(x) for x in input().split(',')]
if n >= len(lst):
    print("error")
else:
    notic = lst[n]
    lst += [notic] * m
    print(lst)



