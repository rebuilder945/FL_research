a = eval(input())
m,n = eval(input())
if n<len(a)-1:
    del a[m:n]
    print(a)
if n>len(a)-1 or m>n:
    print('error')
