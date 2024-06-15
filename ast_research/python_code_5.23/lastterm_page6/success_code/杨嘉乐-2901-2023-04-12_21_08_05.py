sum=0
i=0
while 1:
    n=eval(input())
    if type(n)==int:
        sum+=n
        i+=1
    elif type(n)==str:
        break
print("%d %d"%(i,sum))
