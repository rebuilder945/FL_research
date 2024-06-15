n=str(input())
alpha=0
digit=0
space=0
other=0
for i in n:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
print(alpha,space,digit,other)
    
