a=input()
b=input()
c=[a,b]
d=['red','blue','yellow']
h0=['red','blue']
h1=['red','yellow']
h2=['blue','yellow']
m=1
if set(c).issubset(set(d)) and len(set(c))==2:
    m=0
if set(c)==set(h0):
    print('purple')
if set(c)==set(h1):
    print('orange')
if set(c)==set(h2):
    print('green')
if m==1:
    print('error')
