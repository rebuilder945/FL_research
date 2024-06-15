def sushu(s):
    if s > 3 :
        for x in range(2,s//2+1):
            if s % x==0:
                return False
        return True
    elif s==3:
        return True
    elif s == 2:
        return True
    else:
        return False
a = eval(input())
b = []
for i in range(len(a)):
    if sushu(a[i]):
        b.append(a[i])
print(b)


