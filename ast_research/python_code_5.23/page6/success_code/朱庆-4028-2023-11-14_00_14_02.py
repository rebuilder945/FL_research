def sushu(n):
    if n>1:
        for x in range(2,n):
            if n%x==0:
                return False
    return n
def huiwenshu(m):
    s = str(m)
    if m == s[::-1]:
        return True
    else:
        return False
n = eval(input())
if type(n)!=type(1) or int(n)<1:
    print("illegal input")
else:
    hui = []
    for i in range(2,n):
        if sushu(i) and huiwenshu(i)==i:
            hui.append(i)
for x in range(len(hui)):
    print("%d"%hui[x],end='')

            




