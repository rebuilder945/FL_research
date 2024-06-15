def sushu(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return 1
def huiwenshu(n):
    num = str(n)
    s = num[::-1]
    if num == s:
        return n
x = float(input())
if (x - int(x)) > 0:
    print("illegal input")
if x < 1:
    print("illegal input")
else:
    x = int(x)
    hui = []
    s = 2
    for x in range(2,x):
        if sushu(x) and huiwenshu(x) == x:
            hui.append(x)
    for x in range(len(hui)):
        print("%d"%hui[x],end = '')
