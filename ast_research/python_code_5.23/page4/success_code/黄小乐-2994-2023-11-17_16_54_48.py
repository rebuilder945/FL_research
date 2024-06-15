ls = input().split(",")
n,m = input().split(",")
ls = list(ls)
n = int(n)
m = int(m)
l = int(len(ls))
if n>= l:
    print("error")
else:
    num=ls[n]
    for i in range(m):
        ls.append(num)
    print(ls)

        

