def s(x):
    for i in range(2,x):
        if x%i==0:
            return 0
    if x==0 or x==1:
        return 0
    return 1
def h(x):
    c=[int(y) for y in str(x)]
    if c==c[::-1]:
        return 1
    return 0
n=eval(input())
l=[]
if n!=int(n) or n<=1:
    print("illegal input")
else:
    for i in range(n):
        if s(i)==1 and h(i)==1:
            l.append(i)
print(*l)


















