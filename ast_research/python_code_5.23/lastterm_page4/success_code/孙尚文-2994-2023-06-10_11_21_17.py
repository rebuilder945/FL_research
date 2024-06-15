a=input().split(",")
b=[]
for i in a:
    i=eval(i)
    b.append(i)

c,d=eval(input())

if -len(a)<=c<len(a):
    e=int(b[c])
    for i in range(d):
        b.append(e)
    print(b)

else:
    print("error")
