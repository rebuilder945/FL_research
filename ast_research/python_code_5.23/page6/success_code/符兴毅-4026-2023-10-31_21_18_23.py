num = int(input())
sum = 0
fengzi = 1
fengmu = 1
for i in range(num):
    b_fengmu = fengmu
    fengmu = fengzi
    fengzi = fengzi+b_fengmu
    n = fengzi/fengmu
    sum += n
print('%.4f'%sum)
