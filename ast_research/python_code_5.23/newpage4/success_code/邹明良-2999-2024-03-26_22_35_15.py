s = input()
n,m = map(int,input().split(" "))
ls = s.split(" ")
len = len(ls)
if n<0:
    n = len+n
if m<0:
    m = len+m
ls[n],ls[m] = ls[m],ls[n]
print(ls)
