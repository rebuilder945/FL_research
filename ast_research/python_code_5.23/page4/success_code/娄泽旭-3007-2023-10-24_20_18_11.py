lst = eval(input())
n,m = eval(input())
if n<=m and m<=len(lst):
    for i in range(m-n):
        lst.remove(lst[n])
    print(lst)
elif n>m or m>len(n):
    print("error")
