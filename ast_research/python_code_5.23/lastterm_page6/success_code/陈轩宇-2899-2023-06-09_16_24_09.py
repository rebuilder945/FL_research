q = input().split()
n,m = int(q[0]),int(q[1])
list1 = []
jishu = 0
if n>0 and m<=10 and (m-n)>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    jishu = 100*a+10*b+c
                    print(jishu,end=' ')
elif n==0 and m<=10 and (m-n)>=3:
    for a in range(n+1,m):
        for b in range(n,m):
            for c in range(n,m):
                jishu = 100*a+10*b+c
                print(jishu,end=' ')    
else:
    print("illegal input")

                 
                
                    
