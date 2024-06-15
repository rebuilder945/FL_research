def sushu(m):
    if m >=2 and type(m)==int:
        for x in range(2,m//2+1):
            if m%x==0:
                return False
        return True
    else:
        return False
def huiwen(m):
    if str(m)==str(m)[::-1]:
        return True
    else:
        return False   
a=eval(input())
if a<2 or type(a)!=type(1):
    print("illegal input")
else:
    for x in range(2,a):
        if sushu(x) and huiwen(x):
            print(x,end=" ")
