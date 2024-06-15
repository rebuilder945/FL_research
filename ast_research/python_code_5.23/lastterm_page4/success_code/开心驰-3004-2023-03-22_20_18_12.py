def susu(n):
    if n<2:
        return False
    for i in range(2,i):
        if n%i==0:
            return False
    return True
a=eval(input())
b=[x for x in a if susu(x)]
print(b)
