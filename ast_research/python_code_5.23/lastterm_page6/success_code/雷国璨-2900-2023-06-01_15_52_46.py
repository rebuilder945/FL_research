n=eval(input())
if type(n)==int:
    for i in range(2,n):
        k=2
        while k<i:
            r=i%k
            if r==0:
                break
            else:
                k+=1
        for x in range(len(i)//2):
            if(i[x]!=i[-(x+1)]):
                break
            else:
                print(i,end=' ')
else:
    print("illegal input")
