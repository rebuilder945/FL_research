l = input().split(",")
n,m = map(int,input().split(","))
a = len(l)-1
if n<a and m<a:
    b = l[n]
    l[n] = l[m]
    l[m] = b
    print(l)
