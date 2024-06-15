n=int(input())
k=2
if n>1 and n%1==0:
    while k<n:
        r=n%k 
        if r==0:
            for i in range(len(str(n))//2):
                if n==k and n[i]==n[-i-1]:
                    print(n,end="")
            break
        else:
            k+=1
else:
    print("illegal input")
