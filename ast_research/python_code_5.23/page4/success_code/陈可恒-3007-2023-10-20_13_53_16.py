a = eval(input())
m,n = eval(input())
if n<len(a)-1 and m<=n:
    del a[m:n]
    print(a)
if n>len(a)-1 or m>n:
    print('error')
# [23, 34, 45, 56, 67, 78, 89]
# 9 2

    

