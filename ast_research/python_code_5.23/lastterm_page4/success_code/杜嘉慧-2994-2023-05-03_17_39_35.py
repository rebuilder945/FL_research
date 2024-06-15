lst = [int(x) for x in input().split(',')]
n,m = [int(x) for x in input().split(',')]
if n >= len(lst):
    print("error")
else:
    notic = lst[n]
    lst.append([notic]*m)
    print(lst)



