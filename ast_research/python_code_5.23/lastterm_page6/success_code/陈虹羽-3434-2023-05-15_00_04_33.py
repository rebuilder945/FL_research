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
    
    if c==p:
        print('purple')
    elif c==o:
        print('orange')
    else:
        print('green')
