mima=list(input())
lst=[0,0,0,0,0]
for x in mima:
    if '0'<=x<='9':
        lst[0]=1
    if 'a'<=x<='z':
        lst[1]=1
    if 'A'<=x<='Z':
        lst[2]=1
    if x in '~!@#$%^&*()_=-/,.?<>;:[]{}|\\':
        lst[4]=1
if len(mima)>=8:
    lst[3]=1
print(sum(lst))
    
    

