A=eval(input())
B=[]
for i in A:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        B.append(i)
print(B)


