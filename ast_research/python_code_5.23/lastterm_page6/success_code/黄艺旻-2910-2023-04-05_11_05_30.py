h = eval(input())
N = eval(input())
b = []
for i in range(1,N+1):
    h = h/2
b.append(h)
num = sum(b)
print('%.2f'%num)
