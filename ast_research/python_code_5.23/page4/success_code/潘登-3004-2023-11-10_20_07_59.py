def sushu(n):
    if n >= 2 and type(n) == int:
        for i in range(2,n//2+1):
            if n % i == 0:
                return False
        return True
    else:
        return False
n=eval(input())
s=[]
s.append(sushu(n).split(','))
print(s)            
