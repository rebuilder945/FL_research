A=eval(input())
B=[]
if 2 in A:
    A.remove(2)
else:
    for x in A:
        for i in range(2,x-1) :
            if  x % i > 0:
                B.append(x)
            else:
                pass
B.append(2)
print(B)


