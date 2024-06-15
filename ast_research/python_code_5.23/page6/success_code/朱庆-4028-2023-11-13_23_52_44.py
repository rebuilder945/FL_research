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
hui=[]
if n<2 or type(n) !=type(1):
    print("illegal input")
else:
    for i in range(2,n):
        if huiwenshu(i) and sushu(i)==i:
            hui.append(i)
    for i in range(len(hui)):
        print(hui[i],end='')        
            




