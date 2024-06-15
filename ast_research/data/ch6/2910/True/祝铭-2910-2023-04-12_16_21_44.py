m = 0
h = eval(input())
times = eval(input())
for i in range(times):
    m = m + h
    h = h/2
    m = m + h
m = m - h
print('%.2f'%(m))
