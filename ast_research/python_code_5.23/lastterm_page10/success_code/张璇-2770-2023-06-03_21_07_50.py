a=list(input())
b=list(input())
f=[]
for x in range(len(a)):
    c=a.count(a[x])
    d=b.count(a[x])
    if c==d:
        f.append('1')
    
if len(f)==len(a):
    print('True')
else:
    print('False')
