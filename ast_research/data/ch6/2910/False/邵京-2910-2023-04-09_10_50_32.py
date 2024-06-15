h=eval(input())
n=eval(input())
s=h
for i in range(n):
    d=h*0.5**i
    s+=d
print('%.2f'%s)
