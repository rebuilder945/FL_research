A=[]
a=[]
while True:
    b=input()
    if b=='ok':
        break
    else:
        b=b.split("")
        A.append(b[0])
        a.append(int(b[1]))
A.sort()
a.sort()
print(A)
print(a)
if 'India'in A:
    print('yes')
else:
    print('no')
print(sum(a))
