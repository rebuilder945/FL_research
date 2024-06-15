def shusu(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return False
    return True
a = eval(input())
c = []
for x in a:
        if shusu(x)==True:
            c.append(x)
print(c)





    







