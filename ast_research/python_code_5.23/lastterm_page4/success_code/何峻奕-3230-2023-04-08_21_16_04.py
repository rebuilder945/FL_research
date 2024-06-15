n=eval(input())
n.sort(reverse=True)
m=[str(i) for i in n]
a=''.join(m)
if a==000:
    print(0)
if a!=0:
    print(a)
