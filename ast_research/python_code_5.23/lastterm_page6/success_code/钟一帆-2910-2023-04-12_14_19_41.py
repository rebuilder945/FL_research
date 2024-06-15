h=eval(input())
t=eval(input())
s=h
for i in range(t-1):
    s+=h
    h*=0.5
print('%.2f'%s)
