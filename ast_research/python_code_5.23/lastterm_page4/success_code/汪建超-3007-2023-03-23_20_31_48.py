lst = eval(input())
n,m = eval(input())
if m < len(lst) and n <len(lst):
    for i in range(n,m):
        del lst[i]
    print(lst)
else:
    print("error")
