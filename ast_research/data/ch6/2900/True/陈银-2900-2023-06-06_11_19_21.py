def huiwenshu(i):
    if str(i)[::1]==str(i)[::-1]:
        return True
def shushu(i):
    for x in range(2,i//2+1):
        if i%x==0:
            return False
    return True
num = eval(input())
if num<2 or num%1!=0:
    print("illegal input")
else:
    for x in range(2,num):
        if huiwenshu(x) and shushu(x):
            print(x,end=" ")


