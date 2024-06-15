def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
num = eval(input())
pList = []
if type(num) != int or num <= 1 :
    print("illegal input")
else:
    for iNum in range(2,num+1):
        sNum = str(iNum)
        if sNum == sNum[::-1] and isPrime(iNum):
            pList.append(str(iNum))
print(" ".join(pList))
