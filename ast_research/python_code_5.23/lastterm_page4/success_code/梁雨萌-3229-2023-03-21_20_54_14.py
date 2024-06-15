lis1=eval(input())
lis2=[]
for i in lis1:
    if lis1.count(i)==1:
        lis2.append(i)
if len(lis2)!=0:
    word=",".join(map(str,lis2))
    print(word)
else:
    print("False")
