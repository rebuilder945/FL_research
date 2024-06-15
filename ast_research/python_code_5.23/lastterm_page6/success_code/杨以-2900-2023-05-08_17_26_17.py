def isprime(n):
    for x in range(2,int(eval(n)**0.5)):
        if x%eval(n)==0:
            return False
        else:
            return True
n=input()
ls=[]
if type(eval(n))==float or eval(n)<1:
    print('illegal input')
else:
    for x in range(2,eval(n)+1):
        j=list(str(x)) 
        j.reverse()
        p=''
        for y in range(0,len(j)):
            p=p+j[y]
        if int(p)==x and isprime(p):
            ls.append(x)
            print(x)
print(ls)
            


