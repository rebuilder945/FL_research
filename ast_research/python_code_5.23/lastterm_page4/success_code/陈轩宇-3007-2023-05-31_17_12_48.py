a = eval(input())
n,m = eval(input())
for i in range(0,len(a)):
    if i in range(n+1,m+1):
        a.remove(i)
        print(a)
    if n+1<0 or m+1>len(a) or n>m:
        print("error")

