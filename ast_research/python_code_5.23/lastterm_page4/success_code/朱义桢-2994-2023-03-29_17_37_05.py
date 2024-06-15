a=list(eval(input()))
n,m=eval(input())
if n not in range(-len(a),len(a)-1):
    print("error")
else:
    b=a[n]
    a.remove(b)
    for i in range(m):
        a.append(b)
    print(a)
