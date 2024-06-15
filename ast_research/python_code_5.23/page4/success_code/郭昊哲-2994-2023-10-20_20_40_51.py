a=(list(eval(input())))
n,m=eval(input())
if n>=0 and n>len(a) or n<0 and n*(-1)>len(a):
    print("error")
else:
    for i in range(m):
        a.append(a[n])
    print(a)








