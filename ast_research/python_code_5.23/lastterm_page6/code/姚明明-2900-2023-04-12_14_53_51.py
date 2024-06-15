n=eval(input())
if n>0 and type(n)==int:
    for i in range(2,n+1):
        count=0
        for m in range(2,i):
            if i%m==0:
                count+=1
            continue
        if count==0:
            s=str(i)
            if s==s[::-1]:
                print(s,end"")
else:
    print("illegal input")

