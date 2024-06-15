n=eval(input())
if n%1==0 and n>0:
    for i in range(0,n):
        while i[::-1]==i:
            for j in range(2,i):
                if (i%j==0):
                    break
                else:
                    print(i)
else:
    print("illegal input")    
