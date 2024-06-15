def su(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i==0:
           return False
    return True
def xuan(lse):
    er=[]
    for num in lse:
        if su(num):
            er.append(num)
    return er
t=eval(input())
h=xuan(t)
print(h)
