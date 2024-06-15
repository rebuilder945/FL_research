a=input()
star=[0,0,0,0,0]
for i in a:
    if i.isnumeric():
        star[0]=1   
    if i.islower():
        star[1]=1 
    if i.isupper():
        star[2]=1
    if i in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\" :
        star[3]=1
if len(a)>8:
    star[4]=1

print(star.count(1))
