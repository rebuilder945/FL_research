mima=input()
ls=list("~!@#$%^&*()_=-/,.?<>;:[]{}|\ ")
count1,count2,count3,count4=0,0,0,0
for x in mima:
    if count1==0:
        if x.isdigit():
            count1+=1
    if count2==0:
        if x.isalpha():
            if x.isupper():
                count2+=1    
    if count3==0:
        if x.isalpha():
            if x.islower():
                count3+=1
    if count4==0:
        if x in ls:
            count4+=1
leval=count1+count2+count3+count4
if len(mima)>=8:
    leval+=1

print(leval)

