a=input()
b=[int(i) for i in a.split(",")]
n,m=eval(input())
if n<=len(b):
    c=b[n]
    for i in range(m):
        b.append(c)
    print(b)
else:
    print("error")

