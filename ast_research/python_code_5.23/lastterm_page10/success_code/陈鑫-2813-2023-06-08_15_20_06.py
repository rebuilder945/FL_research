a=input()
c=input()
b=list(a)
for i in b:
    if i==c:
        b.remove(i)
print(''.join(b))
        


