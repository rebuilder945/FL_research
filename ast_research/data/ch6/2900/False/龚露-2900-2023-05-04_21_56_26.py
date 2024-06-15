def sushu(i):
    for x in range(2,int(i/2+1)):
        if i%x==0:
            break
        else:
            return True
def huiwenshu(i):
    ls = str(i).split()
    ls1=reversed(ls)
    a = ''.join(ls1)
    if int(a)==int(i):
        return True
    else:
        return False
n = eval(input())
if n%1!=0 or n<0:
    print("illegal input")
else:
    for i in range(n):
        if sushu(i) and huiwenshu(i):
            print(i,end=" ")
