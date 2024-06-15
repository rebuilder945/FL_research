n=list(input())
y,k,s,q=0,0,0,0
for i in n:
    if chr(97)<=i<=chr(122) or chr(65)<=i<=chr(90):
        y+=1
    elif i==' ':
        k+=1
    elif chr(48)<=i<=chr(57):
        s+=1
    else:
        q+=1
print(y,k,s,q)
