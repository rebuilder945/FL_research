a = list(eval(input()))
b,c = eval(input())
if b<-len(a):
    print("error")
elif b>len(a):
    print("error")
else:
    d = a[b]
    for i in range(c):
        a.append(d)
    print(a)
