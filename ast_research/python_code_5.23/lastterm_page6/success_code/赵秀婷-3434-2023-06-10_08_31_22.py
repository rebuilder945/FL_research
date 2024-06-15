# 颜色混合器
c1=eval(input)
c2=eval(input)
if (c1,c2)==('red','blue') or (c1,c2)==('blue','red'):
    print('purple')
elif (c1,c2)==('red','yellow') or (c1,c2)==('yellow','red'):
    print('orange')
elif (c1,c2)==('blue','yellow') or (c1,c2)==('yellow','blue'):
    print('green')
else:
    print('error')
