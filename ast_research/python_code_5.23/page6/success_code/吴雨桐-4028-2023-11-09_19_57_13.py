def sushu(n):
    if n>=2 and type(n)==int:
        for x in range(2,n//2+1):#若仅仅是n//2那么n=4时将把4判断为一个素数
            if n%x==0:
                return False
        return True
    else:
        return False
    
def hui(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
    
n=eval(input())
if n<2 or type(n)!=int:
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i) and hui(i):
            print(i,end=' ')
