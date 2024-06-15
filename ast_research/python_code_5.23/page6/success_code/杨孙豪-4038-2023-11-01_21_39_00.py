x=input()
lst=[a for a in x]
y=x.split(' ')
y=''.join(y)
bst=[a for a in y]

a=0
b=len(lst)-len(bst)
c=0
d=0
for i in bst:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        a=a+1
    elif i in '1234567890':
        c=c+1
    else:
        d=d+1
print(a,b,c,d)
