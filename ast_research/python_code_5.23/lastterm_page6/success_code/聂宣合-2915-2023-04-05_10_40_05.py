dex=int(input())
test=[]
for sum in range(0,dex+1):                                    
    if sum>=100:
        sum=str(sum)
        a=int(sum[0])
        b=int(sum[1])
        c=int(sum[2])
        if a**3+b**3+c**3==int(sum):
            test.append(sum)
            print(sum)
if test==[]:
    print("none")
