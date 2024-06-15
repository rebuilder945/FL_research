a=eval(input())
n,m=eval(input())
b=list(a)
if n>len(b):
    print("error")
else:
    c=[b[n]]*m
    for x in c:
        b.append(x)
    print(b)

