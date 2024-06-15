s=input()
count1,count2,count3,count4=0,0,0,0
for x in s:
    if "a"<=x<="z" or "A"<=x<="Z":
        count1=count1+1
    elif x==" ":
        count2=count2+1
    elif "0"<=x<="9":
        count3=count3+1
    else:
        count4=count4+1
print("count1,count2,count3,count4")
   
