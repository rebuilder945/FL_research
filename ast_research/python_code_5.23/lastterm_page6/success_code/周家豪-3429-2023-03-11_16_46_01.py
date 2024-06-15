a=input()
n1,n2,n3,n4=0,0,0,0
for i in a:
    if (i >= 'a' and i <='z') or ( i >='A' and i <='Z'):
        n1+=1
    elif i ==" ":
        n2+=1
    elif i  in '0123456789':
        n3+=1
    else:
        n4+=1
print(n1,n2,n3,n4)

