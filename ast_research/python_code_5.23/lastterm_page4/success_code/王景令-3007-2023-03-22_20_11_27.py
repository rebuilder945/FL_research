lst = eval(input())
a,b = (eval(input()))
n,m = min(a,b),max(a,b)

if m > len(lst) or n > len(lst):
    print("error")
else:
    for i in range(m-n):
        lst.pop(n)
print(lst)


