a2=eval(input())
a1=list(a2)
n,m=eval(input())
if n>len(a1):
    print("error")
else:
    for i in range(m):
        a1.append(a1[n])
    print(a1)

