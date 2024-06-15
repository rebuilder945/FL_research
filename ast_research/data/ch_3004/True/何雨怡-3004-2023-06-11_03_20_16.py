def jude(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
ls = eval(input())
ls1 =[i for i in ls if jude(i)]
print(ls1)
