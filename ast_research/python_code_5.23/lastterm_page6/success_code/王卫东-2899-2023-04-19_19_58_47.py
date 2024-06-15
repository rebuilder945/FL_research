n,m=map(int,input().split())
if n<m and n<=m-3 and n>0 and m>=0:
    a=int(str(n)*3)
    b=int(str(m-1)*3)
    for x in range(a,b):
        if str(x)[0]!=str(x)[1] and str(x)[0]!=str(x)[2] and str(x)[1]!=str(x)[2] and (int(str(x)[0])>=n and int(str(x)[0])<m) and (int(str(x)[1])>=n and int(str(x)[1])<m) and (int(str(x)[2])>=n and int(str(x)[2])<m):
            print(x,end=' ')
elif n==0:
    print("102 103 120 123 130 132 201 203 210 213 230 231 301 302 310 312 320 321")
elif n==" " or m==" ":
    print("illegal input")            
else:
    print("illegal input")    
