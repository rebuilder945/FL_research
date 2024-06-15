lst1 = list(eval(input()))
n,m = eval(input())
if n > len(lst1):
    print("error")
else:
    lst2 = lst1 + [lst1[n]] * m
    print(lst2)

