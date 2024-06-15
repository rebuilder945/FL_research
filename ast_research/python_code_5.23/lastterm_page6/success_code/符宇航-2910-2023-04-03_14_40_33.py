h = eval(input())
N = eval(input())
s = h
N = N-1
for i in range(N):
    s+=h
    h = h/2
print('%.2f'%s)

