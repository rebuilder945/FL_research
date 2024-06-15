str=eval(input())
alpha=0
space=0
digit=0
other=0
for i in str:
    if str.isalpha():
        alpha+=1
    elif str.isspace():
        space+=1
    elif str.isdigit():
        digit+=1
    else:
        other+=1
print(alpha,space,digit,other)
