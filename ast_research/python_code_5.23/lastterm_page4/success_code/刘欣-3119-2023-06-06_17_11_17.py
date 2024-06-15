lis=eval(input())
lis1=[]
for i in range(len(lis)-1,-1,-1):
    if lis[i] not in lis1:
        lis1.append(lis[i])
lis1.reverse()
print(lis1)
