lis=eval(input(''))
lis.reverse()
lis1=[]
for i in lis:
    if i not in lis1:
        lis1.insert(0,i)
print(lis1)

