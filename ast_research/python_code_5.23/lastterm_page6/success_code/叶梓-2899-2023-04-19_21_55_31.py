s=input().split(" ")
n=int(s[0])
m=int(s[1])
if m-n>=3 and 10>n>=0 and m<=10:
    if n!=0:
        for x in range(n,m):
            for y in range(n,m):
                for z in range(n,m):
                    if x!=y and y!=z and x!=z:
                        a=x*100+y*10+z
                        print(a,end=" ")
    else:
        for x in range(n+1,m):
            for y in range(n,m):
                for z in range(n,m):
                    if x!=y and y!=z and x!=z:
                        a=x*100+y*10+z
                        print(a,end=" ")
else:
    print("illegal input")

