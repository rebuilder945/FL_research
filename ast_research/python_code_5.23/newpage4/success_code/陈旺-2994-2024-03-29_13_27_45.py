a=input()
b=[int(i) for i in a.split(",")]
n,m=eval(input())
c=b[n]
if n<=len(b):
    for i in range(m):
        b.append(c)
    print(b)
else:
    print("error")

