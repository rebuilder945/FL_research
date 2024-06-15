a = input()
n1 = 0
n2 = 0
n3 = 0
n4 = 0
for i in a:
    if i.isalpha():
        n1+=1
    elif i.isspace():
        n2+=1
    elif i.isdigit():
        n3+=1
    else:
        n4+=1
print(n1,n2,n3,n4,end='')
