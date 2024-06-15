def sushu(n):
    if(n >= 2):
        for i in range(2,n):
            if(n%i == 0):
                return False
        else:
            return True
    else:
        return False
a = eval(input())
b = []
for i in a:
    if(sushu(i)):
        b.append(i)
print(b)
