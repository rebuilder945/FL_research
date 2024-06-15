A=eval(input())
for x in A:
    for i in range(2,x-1) :
        if  x % i == 0:
            A.remove(x)
        else:
            pass
print(A)


