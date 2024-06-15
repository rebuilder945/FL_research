a=eval(input())
n,m=(eval(input()))
b=[]
b+=a
if n<=len(a)-1:
    for i in m:
        b.append(a(n))
    print(b)
else:
    print('error')
