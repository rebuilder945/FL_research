a = list(eval(input()))
n,m = eval(input())
if n>len(a)-1 and n>0:
    print("error")
elif n<0 and n<-len(a):
    print("error")
else:
    for i in range(m):
        a.append(n+1)
    print(a)
