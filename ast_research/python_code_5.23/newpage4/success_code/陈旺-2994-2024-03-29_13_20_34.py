a=input()
b=[int(i) for i in a.split(",")]
n,m=eval(input())
if n<=len(b):
    for i in range(m):
        b.append(b[n])
    print(b)
else:
    print("error")

