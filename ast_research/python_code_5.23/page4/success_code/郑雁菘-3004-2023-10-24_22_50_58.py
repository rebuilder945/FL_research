A = eval(input())
B=[]
k = 0
for i in A:
    for j in range(2,i+1):
        if i // j ==1:
            k +=1
            if k == 2:
                B.append(i)
print(B)
print(A)
print(i)
        


       


