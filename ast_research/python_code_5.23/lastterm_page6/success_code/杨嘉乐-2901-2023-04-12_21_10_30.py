sum=0
i=0
while 1:
    n=input()
    if n=='#':
        break
    else:
        sum+=int(n)
        i+=1
print("%d %d"%(i,sum))
