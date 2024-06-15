ls = input().split()
n,m=input().split(",")
if -len(ls)<=int(n)<=len(ls)-1:
    a=ls[n]
    for x in range(int(m)):
        ls.append(a)
    print(ls)
else:
    print("error")
