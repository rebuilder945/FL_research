def fuck(o):
    for i in range(o-2):
        if o%(i+2)==0:
            return 0
    return 1
def ass(o):
    n=o
    l=[]
    while(n!=0):
        l.append(n%10)
        n=n//10
    if str(l)==str(l.reverse()):
        return 1
    else:
        return 0
n=eval(input())
if n<0 or n%1!=0:
    print('illegal input')
else:
    for i in range(n):
        i+=1
        if fuck(n) or ass(n)

        
