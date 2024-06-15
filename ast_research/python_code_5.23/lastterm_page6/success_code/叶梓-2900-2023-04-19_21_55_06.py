def idPrime(num):
    for j in range(2,int(num)):
        if (num%j==0):
            return False
    else:
        return True
number=eval(input())
num=int(number)
if num>=2 and type(number) is int:
    for i in range(num):
        if idPrime(i) and str(i)==str(i)[::-1] and i>=2:
            print(i,end=" ")
else:
    print("illegal input")
