lis=input()
lis2=[]
lis1=[]
for x in range(len(lis)-1):
    if '1'<=lis[x]<='9':
        lis1.append(lis[x])
    if not '1'<=lis[x+1]<='9' or :
        if len(lis1)>=len(lis2):
            lis2=lis1.copy()
            lis1=[]
for x in lis2:
    print(x,end='')
