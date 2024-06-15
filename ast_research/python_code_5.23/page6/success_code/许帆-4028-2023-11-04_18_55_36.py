def sushu(num):
    b = 2
    lst=[2]
    for i in range(num):
        for x in range(i-3):
            if b < i and i/b == 0:
                break
            elif b < i and i/b != 0:
                b += 1
            elif b == i-1:
                lst.append(i)
    return lst
def huiwen(x):
    lst2=[]
    for i in range(x):
        if i<10:
            lst2.append(i)
        elif i == i//100+(i%10)*100+(i-i//100*100)//10*10:
            lst2.append(i)
    return lst2
            
n = eval(input())
if type(n) == float or n <= 0:
    print("illegal input")
else:
    lst3=[]
    for i in range(1,n+1):
        if i in sushu(n) and i in huiwen(n):
            lst3.append(i)
    print(i for i in lst3)
            

