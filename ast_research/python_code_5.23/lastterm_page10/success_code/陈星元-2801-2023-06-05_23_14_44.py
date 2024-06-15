def secret(str):
    str1="~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
    num,lower,upper,length,character=(0,0,0,0,0)
    if len(str)>=8:
        length+=1
    for x in str:
        if x.isdigit():
            num+=1
        if x.isalpha():
            if x.islower():
                lower+=1
            else:
                upper+=1
        if x in str1:
            character+=1
    return num,lower,upper,length,character
str=input()
rate=0
num,lower,upper,length,character=secret(str)
if num!=0:
    rate+=1
if lower!=0:
    rate+=1
if upper!=0:
    rate+=1
if length!=0:
    rate+=1
if character!=0:
    rate+=1
print(rate)
        
            
