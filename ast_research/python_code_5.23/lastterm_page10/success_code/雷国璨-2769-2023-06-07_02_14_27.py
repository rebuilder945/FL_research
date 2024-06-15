a=' abcdefjhijklmnopqrstuvwxyz'
b=' ABCDEFJHIJKLMNOPQRSTUVWXYZ'
c=input()
print(c)
for i in c:
    if i in a:
        print(a[26-a.index(i)+1],end='')
    elif i in b:
        print(b[26-b.index(i)+1],end='')
    else:
        print(i,end='')
