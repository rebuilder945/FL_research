def isPrime(num): 
    if num==0 or num==1:
        return False
    for j in range(2,int(num**0.5)+1):
        if num%j == 0:
            return False
    else: 
        return True
def huiwen(num):
    if str(num)==str(num)[::-1]: 
        return True
    else:
        return False
n=eval(input())
if type(n)==int and n>1 : 
    lst1=[]
    for i in range(2,n+1):
        if isPrime(i) and huiwen(i):
            lst1.append(i)
    lst1=[str(i) for i in lst1]
    s=" ".join(lst1)
    print(s)
else:
    print("illegal input")
