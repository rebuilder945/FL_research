level=[0,0,0,0,0]
s=str(input())
for i in s:
    if i.isdigit():
        level[0]=1
    elif i.islower():
        level[1]=1
    elif i.isupper():
        level[2]=1
    elif i in '~!@#$%^&*()_=-/,.?<>;:[]{|}\\':
        level[3]=1
if len(s)>=8:
    level[4]=1
print(sum(level))
            
            

