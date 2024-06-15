a = eval(input())
n,m = eval(input())
b = []
b.append(x for x in a)
if n>(len(b)-1):
        print("error")
else:
        c = b[n:n+1]*m
        print(b+c)
