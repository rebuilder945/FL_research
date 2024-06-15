lst = eval(input())
n,m = eval(input())
if n > len(lst) or m > len(lst):
    print("error")
else:
    for i in range(n,m):
        del lst(i)
    print(lst)
