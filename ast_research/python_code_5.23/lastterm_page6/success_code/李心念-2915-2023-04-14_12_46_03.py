a = eval(input())
b = 0
def shuixian(a):
    n = [int(x)**3 for x in str(a)]
    if a == sum(n):
        return True
    else:
        return False
for y in range(2,a+1):
    if shuixian(y):
        print(y)
        b += 1
if b ==0:
    print('none')
