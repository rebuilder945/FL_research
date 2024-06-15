def Fib1(a):
    p, q = 1, 2
    for i in range(a-1):
        p, q = q , p+q
    return p
def Fib2(b):
    p, q = 2, 3
    for i in range(b-1):
        p, q = q , p+q
    return p
n = eval(input())
pList = []
for i in range(1,n+1):
    pList.append(Fib2(i)/Fib1(i))
tSum = sum(pList)
print("%.4f"%tSum)
