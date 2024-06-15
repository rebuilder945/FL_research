a=input().split(',')
n,m=eval(input())
for i in a:
    i=int(i)
if n in range(-len(a),len(a)-1):
    b=a[n]
    a.remove(b)
    for i in range(m):
        a.append(b)
    for i in a:
        i=int(i)
    print(a)
else:
    print("error")
