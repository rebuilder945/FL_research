def sushu(n):
    if n==2:
        return True
    else:        
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
def huiwenshu(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
    
lst=[]
num=eval(input())
if num!=abs(int(num)):
    print('illegal input')
else:
    for i in range(2,num):
        if sushu(i) and huiwenshu(i):
            lst.append(i)
print(' '.join(str(i) for i in lst))
