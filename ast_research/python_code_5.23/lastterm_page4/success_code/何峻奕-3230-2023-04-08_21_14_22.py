n=eval(input())
n.sort(reverse=True)
if n==0:
    print(0)
if n!=0:
    m=[str(i) for i in n]
    a=''.join(m)
    print(a)
