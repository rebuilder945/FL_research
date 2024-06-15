ts="~!@#$%^&*()_=-/,.?<>;:[]{}\|"
lowalpha="abcdefghijklmnopqrstuvwxyz"
upalpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums="0123456789"
star1=0
star2=0
star3=0
star4=0
star5=0

s=input()
if len(s)>=8:
    star1=1
for i in s:
    if i in ts:
        star2=1
    elif i in lowalpha:
        star3=1
    elif i in upalpha:
        star4=1
    elif i in nums:
        star5=1
sum=star1+star2+star3+star4+star5
print(sum)



