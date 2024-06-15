a = list(eval(input()))
b = a.copy()
n,m = eval(input())
if n>len(a)-1 and n>0:
    print("error")
elif n<0 and n<-len(a):
    print("error")
else:
    for i in range(m):
        if n >= 0:
            a.append(b[n+1])
        elif n<0:
            a.append(b[n])
    print(a)
