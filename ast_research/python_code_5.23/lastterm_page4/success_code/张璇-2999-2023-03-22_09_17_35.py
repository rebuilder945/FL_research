a=input()
b,c=eval(input())
f=a.split()
e=f.copy()
if b<len(f)and c<len(f):
    e[b]=f[c]
    e[c]=f[b]
    print(e)
elif b>=len(f)or c>=len(f):
    print(f)
