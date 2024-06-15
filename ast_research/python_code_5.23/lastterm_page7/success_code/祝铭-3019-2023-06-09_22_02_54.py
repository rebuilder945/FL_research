sen = input()
senlist = sen.split(' ')
a = 0
b = 0
for i in range(len(senlist)) :
    a += len(senlist[i])
    b += 1
print(b,end=',')
print('%.2f'%(a / b))
