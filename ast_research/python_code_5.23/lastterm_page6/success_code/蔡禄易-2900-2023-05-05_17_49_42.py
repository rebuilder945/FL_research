def su(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5+1)):
        if n % i == 0:
            return False
    return True
def hui(n):
    if str(n) == str(n)[::-1]:
        return False
    else:
        return True
n = input()   
if type(n) != float and n > 2:
    for i in range(2,n):
        if su(n) and hui(n):
            print(i,end=' ')
else:
    print("illegal input")
    
