n=eval(input())
if n>1 and n%1==0:
    lis=[x for x in range(n)]
    a=lis.copy()
    for i in range(0,len(lis)):
        for j in range(2,(lis[i])):
            if ((lis[i])%j==0) or lis[i]%3==0 or lis[i]%11==0 or lis[i]%7==0 or lis[i]%17==0 or lis[i]%13==0 or lis[i]%5==0 or lis[i]%23==0:
                if lis[i]!=3 and lis[i]!=11 and lis[i]!=7 and lis[i]!=5 and lis[i]!=13 and lis[i]!=23 and lis[i]!=17:
                    a.remove(lis[i])
            break
    if 0 in a:
        a.remove(0)
    if 1 in a:
        a.remove(1)
        
    c=[]
    for i in range(0,len(a)-1):
        b=str(a[i])
        if b[::-1]==b:
            c.append(a[i])
    
    word=str(c[0])
    for i in range(1,len(c)):
        word=word+" "+str(c[i])
    print(word)
else:
    print("illegal input")
            
        
    
