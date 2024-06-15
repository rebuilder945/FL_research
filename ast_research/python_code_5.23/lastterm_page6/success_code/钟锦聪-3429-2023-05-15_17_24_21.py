num = input()
alpha_count,num_count,space_count,other_count = 0,0,0,0
for i in num:
    if "A"<= i<="Z" or "a" <= i <="z":
        alpha_count +=1
    elif i==" ":
        space_count+=1
    elif "0"<=i<="9":
        num_count+=1
    else:
        other_count+=1
print(alpha_count,num_count,space_count,other_count)

    
