color1=input()
color2=input()
s1={color1,color2}
p={'red','blue'}
o={'red','yellow'}
g={'blue','yellow'}
if s1==p:
    print('purple')
elif s1==o:
    print('orange')
elif s1==g:
    print('green')
else:
    print('error')
