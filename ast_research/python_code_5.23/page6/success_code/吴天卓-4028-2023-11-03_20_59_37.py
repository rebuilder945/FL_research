n=eval(input())
C=[]
B=[]
D="2"
if n>1 and int(n)==n:
    for i in range(2,n):
        for e in range(2,i):
            
            C.append(i%e)
        if 0 in C:
            C.clear()
        elif i<10:
            B.append(i)
        elif n>10:
            for j in range(len(str(i))//2):
                if str(i)[j]==str(i)[-1-j]:
                    B.append(i)
    for r in range(len(B)):
        D=D+str(B[r])+" "
    print(D[1:-1])
else:
    print("illegal input")
