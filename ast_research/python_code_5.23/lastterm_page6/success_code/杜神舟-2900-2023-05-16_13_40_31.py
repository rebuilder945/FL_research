def sushu(n):
    if n>=2:
        for x in range(2,n):
            if n%x==0:
                return False
        else:
            return  True
    else:
        return False
def hui(n):
    if n<=1:
        return False
    elif 1<n<10:
        return True
    else:
        if str(n)[0::]==str(n)[::-1]:
            return True
        else:
            return False
n=eval(input())
list1=[]
if n<=1:
    print('illegal input')
else:
    for x in range(n):
        if sushu(x) and hui(x):
            list1.append(x)
    print(' '.join(str(x) for x in list1))

        
