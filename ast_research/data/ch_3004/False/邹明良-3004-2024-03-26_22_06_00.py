def isprime(a):
    if a==1 or a%2==0:
        return False
    else:
        for i in range(a-2):
            if a%(i+2)==0:
             return False
    return True
    


ls = list(eval(input()))
lsPri = []
for i in range(len(ls)):
    if isprime(ls[i]):
        lsPri.append(ls[i])
print(lsPri)
