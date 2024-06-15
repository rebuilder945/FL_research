ls = eval(input())
n,m = input().split(',')
n = int(n)
m = int(m)
if n<len(ls) and m<len(ls):
    if n<m:
        del ls[n:m]
        print(ls)
    else:
        del ls[m+1:n+1]
        print(ls)
else:
    print("error")




