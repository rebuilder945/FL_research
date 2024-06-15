def sushu(n):
    if n < 2:
        return False
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True
def huiwenshu(n):
    n=str(n)
    if n[::-1]==n:
        return True
    return False
def huiwensushu(n):
    lst1=[]
    for i in range(n+1):
        if sushu(i) and huiwenshu(i):
            lst1.append(str(i))
    return lst1
def main():
    n=eval(input())
    if n is float or n <= 0:
        print('illegal input')
    else:
        print(' '.join(huiwensushu(n)))
main()
