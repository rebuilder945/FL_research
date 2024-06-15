h=eval(input())
n=eval(input())
s=[h]
for x in range(n):
    h=0.5*h
    s.append(h)
ss=2*sum(s)-s[0]
print('%.2f'%ss)

