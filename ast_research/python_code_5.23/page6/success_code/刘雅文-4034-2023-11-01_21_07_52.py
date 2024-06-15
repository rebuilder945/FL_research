m=('red','yellow','blue')
a=input()
b=input()
if a in m and b in m:
    if a==m[0] and b==m[1] or a==m[1] and b==m[0]:
        print('orange')
    if a==m[0] and b==m[2] or a==m[2] and b==m[0]:
        print('purple')
    if a==m[1] and b==m[2] or a==m[2] and b==m[1]:
        print('green')
    if a==b:
        print('error')
else:
    print('error')
