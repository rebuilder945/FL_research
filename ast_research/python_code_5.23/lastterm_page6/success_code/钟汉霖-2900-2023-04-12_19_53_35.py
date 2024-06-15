def isP(n):
    for k in range(2,n//2+1):
        if n%k==0:
            return False
        else:
            print("illegal input")
    return True

def hw(s):
    return str(s)==str(s)[::-1]

a=filter(hw,range(2,1000))
b=filter(isP,a)
print(*b)
