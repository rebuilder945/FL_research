lis1='~!@#$%^&*()_=-/,.?<>;:[]{}|\\'
password=input()
n1=1
n3=1
n2=1
n4=1
n5=1
star=0
for x in password:
    if '1'<=x<='9'and n1:
        n1=0
        star+=1
    elif 'a'<=x<='z' and n2:
        n2=0
        star+=1
    elif 'A'<=x<='Z' and n3:
        n3=0
        star+=1
    elif len(password)>=8 and n4:
        star+=1
        n4=0
    elif x in lis1 and n5:
        star+=1
        n5=0
print(star)

