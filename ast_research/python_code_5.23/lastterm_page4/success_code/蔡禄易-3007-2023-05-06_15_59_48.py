lst = eval(input())
n,m = eval(input())
if n not in lst or m not in range(len(lst)):
    print("error")
else:
    for i in range(n,m):
        del(lst[i])
print(lst)
