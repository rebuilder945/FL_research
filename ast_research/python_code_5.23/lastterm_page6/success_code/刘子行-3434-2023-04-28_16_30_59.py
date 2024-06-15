a=input()
b=input()
c=(a,b)
d=('red','green','yellow')
h0=('red','blue')
h1=('red','yellow')
h2=('blue','yellow')
if set(c).issubset(set(d)):
    m=0
else:
    m=1
if c==h0:
    print('purple')
if c==h1:
    print('orange')
if c==h2:
    print('green')
if m==0:
    print('error')
