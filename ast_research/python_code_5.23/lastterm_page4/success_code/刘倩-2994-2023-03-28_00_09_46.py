a = eval(input())
n,m = eval(input())
b = [a]
b.append(x for x in b)
if n>(len(b)-1):
        print("error")
else:
        c = [b[n]]*m
        print(b+c)
