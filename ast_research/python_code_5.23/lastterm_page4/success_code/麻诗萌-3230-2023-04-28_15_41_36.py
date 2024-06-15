lst=list(map(int,input()))
lst.sort(reverse=True)
m=""
for i in lst:
    m+=str(i)
print(m)    
