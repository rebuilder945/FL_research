a=input()
def change(i):
    b='abcdefghijklmnopqrstuvwxyz'
    c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if i in b:
        i=b[25-b.index(i)]
    elif i in c:
        i=c[25-c.index(i)]
    else:
        i=i
    return i
for i in a:
    print(change(i),end='')


