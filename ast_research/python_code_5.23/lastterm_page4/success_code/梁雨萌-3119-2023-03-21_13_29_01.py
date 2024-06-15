lis1=eval(input())
for i in range(len(lis1)-1,-1,-1):
        if lis1.count(lis1[i])>1:
            del lis1[i]
print(lis1)
