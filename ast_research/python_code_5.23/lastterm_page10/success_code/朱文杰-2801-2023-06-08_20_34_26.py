ls=[0,0,0,0,0]
code=input()
str1="~!@#$%^&*()_=-/,.?<>;:[]{}\|"
for i in code:
    if i.isdigit():
        ls[0]=1
    elif i.islower():
        ls[1]=1
    elif i.isupper():
        ls[2]=1
    elif len(code)>=8:
        ls[3]=1
    elif i in str1:
        ls[4]=1
print(sum(ls))
