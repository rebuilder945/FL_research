def isprime(n):
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            return False
    return True
n=input()
if type(eval(n))==float or eval(n)<1:
    print('illegal input')
else:
    l=''
    for x in range(2,eval(n)+1):
        j=list(str(x)) 
        j.reverse()
        p=''
        
        for y in range(0,len(j)):
            p=p+j[y]
        if int(p)==x and isprime(int(x)):
            l=l+str(x)+' '   
    print(l)
        

            


