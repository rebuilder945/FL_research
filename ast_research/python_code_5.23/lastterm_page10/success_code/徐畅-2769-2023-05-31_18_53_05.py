line=list((input()))
lst1=[chr(i) for i in range(ord("a"),ord("a")+27)]
lst2=[chr(i) for i in range(ord("A"),ord("A")+27)]
for i in range(len(line)):
    if line[i] in lst1:
        a=lst1.index(line[i])
        line[i]=lst1[26-a]
    if line[i] in lst2:
        a=lst2.index(line[i])
        line[i]=lst2[26-a]
print(*line,sep='')

        
