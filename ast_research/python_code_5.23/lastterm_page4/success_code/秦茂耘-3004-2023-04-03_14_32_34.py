A=eval(input())
B=[]
for i in A:
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        B.append(i)
if 1 in B:
    B.remove(1)
if 0 in B:
    B.remove(0)
print(B)


