a=eval(input())
def h(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
b=[n for n in a if h(n)]
print(b)





