def sushu(i):
    for x in range(2,i-1):
        if i%x==0:
            return False
    return True
def huiwenshu(i):
    a = str(i)[::-1]
    if int(a)==int(i):
        return True
    else:
        return False
n = eval(input())
if n%1!=0 or n<2:
    print("illegal input")
else:
    for i in range(2,n):
        if sushu(i)==True and huiwenshu(i)==True:
            print(i,end=" ")
