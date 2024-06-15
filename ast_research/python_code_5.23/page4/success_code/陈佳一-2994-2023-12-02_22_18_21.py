a=input().split(',')
b,c=eval(input())
if b>=len(a):
    print("error")
else:
    d=a[b]
    for x in range(c):
        a.append(d)
    e=[]
    for i in a:
        e.append(int(i))
    print(e)
