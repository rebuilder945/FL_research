h=eval(input())
N=eval(input())
a=h
for x in range(N-1):
    a+=h*0.5**x
print('%.2f'%a)
