myarr = input()
def isprime(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        a = False 
        count = n
        for i in range(2, count, 1):
            if n % i == 0:
                a = False
                break
            else:
                a = True
                count = int(n / i) + 1
        return a
if __name__ == '__main__':
    print("[",end=''"]")
    for i in myarr:
        if isprime(i) == True:
              print("[",i, end=' '"]")

