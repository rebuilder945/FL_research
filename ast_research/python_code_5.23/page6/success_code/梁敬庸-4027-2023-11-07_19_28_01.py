sum=0
num=0
while True:
    a=input()
    if a!="#":
        a=int(a)
        sum+=a
        num+=1
    else:
        break    
print("%d %d"%(num , sum))
