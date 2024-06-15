lst = eval(input())
n, m =eval(input())
if n <= len(lst):
    for i in range(n,m):
        lst.pop(i)
    print(lst)
else:
    print("error")
