a=input()
num=0
num1=0
num2=0
num3=0
strong=0
for i in a:
    if i.isdigit():
        num+=1
if num!=0:
    strong+=1
for i in a:
    if i.isalpha():
        if i.isupper():
            num1+=1
if num1!=0:
    strong+=1
for i in a:
    if i.isalpha():
        if i.islower():
            num2+=1
if num2!=0:
    strong+=1
if len(a)>=8:
    strong+=1
for i in a:
    if i in "~!@#$%^&*()_=-/,.?<>;:[]{}|\" :
        num3+=1
if num3!=0:
    strong+=1
print(strong)
