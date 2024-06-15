line=list((input()))
c=line.copy()
lst1=[chr(i) for i in range(ord("a"),ord("a")+26)]
lst2=[chr(i) for i in range(ord("A"),ord("A")+26)]
for i in range(len(line)):
    if line[i] in lst1:
        a=lst1.index(line[i])
        line[i]=lst1[25-a]
    if line[i] in lst2:
        a=lst2.index(line[i])
        line[i]=lst2[25-a]
print(*c,sep='')
print(*line,sep='')

        
