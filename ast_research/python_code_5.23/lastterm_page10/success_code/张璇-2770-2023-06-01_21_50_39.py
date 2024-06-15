a=list(input())
b=list(input())
for x in range(len(a)):
    d=a[x]
    b.pop(d)
if b==[]:
    print('True')
else:
    print('False')
