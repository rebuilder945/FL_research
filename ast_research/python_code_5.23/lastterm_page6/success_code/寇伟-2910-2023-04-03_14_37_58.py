h=eval(input())
N=eval(input())
total=0
for i in range(N):
    if i == 0:
        total+=h
    else:
        total+=h*(0.5)**i*2
print('%.2f'%total)





