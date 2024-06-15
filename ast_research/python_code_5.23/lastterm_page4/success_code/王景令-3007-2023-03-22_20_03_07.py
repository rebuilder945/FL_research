lst = eval(input())
n.m = eval(input())
if m > len(lst) or n > len(lst):
    print("error")
else:
    for i in range(n-m):
        lst.pop(n)
print(lst)


