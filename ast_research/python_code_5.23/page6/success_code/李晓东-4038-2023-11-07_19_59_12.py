list = input()
count1=0
count2=0
count3=0
count4=0
for i in list:
    if "a"<=i<="z" or "A"<=i<="Z" :
        count1 = count1 +1
    elif i  ==" ":
        count2 = count2+1
    elif "0"<=i<="9":
        count3 = count3+1
    else :
        count4 = count4+1
print(count1,count2,count3,count4)


