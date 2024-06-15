ls=eval(input())
n,m=eval(input())
if n<=m and n>0 and m<len(ls):
    while n<m:
        ls.remove(ls[n])
        m-=1
    print(ls)
else:
    print("error")
