def shushu(i):
    for x in range(2,i//2+1):
        if i % x == 0:
            return False
       
    return True
def huiwenshu(i):
    if str(i)[::1]==str(i)[::-1]:
        return True
a = eval(input())
if a < 2 or type(a)!=type(1):
    print("illegal input")
else:
    for x in range(2,a):
        if shushu(x) and huiwenshu(x):
            print(x,end=" ")
   
    

    

