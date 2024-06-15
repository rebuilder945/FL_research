ls=eval(input())
b=0
while len(ls)>0:
    a=max(ls)
    b=a*10**len(ls)+b
    ls.remove(a)
print(b)
