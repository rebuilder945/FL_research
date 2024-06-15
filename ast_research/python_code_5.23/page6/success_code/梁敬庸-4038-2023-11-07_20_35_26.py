str=input()
num=0
w=0
k=0
d=0
for x in str:
    if x>='0' and x<='9':
        num+=1
    elif x>='a' and x<='z' and x>='A' and x<='Z':
        w+=1
    elif x==' ':
        k+=1
    else:
        d+=1
print("%d %d %d %d"%(w,k,num,d))
