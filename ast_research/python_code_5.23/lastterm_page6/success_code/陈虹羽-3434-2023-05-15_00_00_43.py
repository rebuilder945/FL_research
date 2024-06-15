a=input()
b=input()
c={a,b}
p={'red','blue'}
o={'yellow','red'}
g={'blue','yellow'}
s={'blue','yellow','red'}
if a==b or a not in s or b not in s:
    print('error')
else:
    s1={a,b}
    if s1==p:
        print('purple')
    elif s1==o:
        print('orange')
    else:
        print('green')
