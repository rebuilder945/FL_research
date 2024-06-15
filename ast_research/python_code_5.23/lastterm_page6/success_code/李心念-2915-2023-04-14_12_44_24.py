a = eval(input())
def shuixian(a):
    n = [int(x)**3 for x in str(a)]
    if a == sum(n):
        return True
    else:
        return False
for y in range(1,a+1):
    if shuixian(y):
        print(y,end=' ')
