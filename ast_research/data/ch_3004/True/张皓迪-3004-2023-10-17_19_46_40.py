def g_prime(num):
    if num<2:
        return False
    for x in range(2,int(num**0.5)+1):
        if num%x==0:
            return False
    return True
def f_prime(ls):
    pr=[]
    for num in ls:
        if g_prime(num):
            pr.append(num)
    return pr
ls=eval(input())
pr=f_prime(ls)
print(pr)

    
