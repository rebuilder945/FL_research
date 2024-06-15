color1=input()
color2=input()
sl={color1,color2}
p={'red','blue'}
o={'red','yellow'}
g={'blue','yellow'}
t={'yellow','red','blue'}
if color1 not in t or color2 not in t or color1 ==color2:
    print('error')
elif sl==p: 
    print("purple")
elif sl==o:
    print("orange")
else:
    print("green")

