n=eval(input())
C=[]
B=[]
if n>1:
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
    print(B[:])
else:
    print("illegal input")
