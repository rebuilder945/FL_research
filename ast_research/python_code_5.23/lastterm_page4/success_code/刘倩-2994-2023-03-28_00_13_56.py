a = eval(input())
n,m = eval(input())
b = a.split(',')
b.append(x for x in b)
if n>(len(b)-1):
        print("error")
elif n<len(b):
        c = [b[n]]*m
        print(b+c)
