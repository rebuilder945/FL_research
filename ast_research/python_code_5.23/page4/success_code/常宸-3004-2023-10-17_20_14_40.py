def Su(n):
    if(n>=2):
        for i in range(2,n):
            if (n%i==0):
                return False
        return True
    else:
        return False
a = eval(input())
save = []
for i in a:
    if (Su(i)):
        save.append(i)
print(save)
