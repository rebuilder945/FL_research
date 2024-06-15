s=input()
char_count,space_count,num_count,other_count=0,0,0,0
for i in s:
    if "a"<=i<="z"or"A"<=i<="Z":
        char_count+=1
    elif "0"<=i<="9":
        num_count+=1
    elif i==" ":
        space_count+=1
    else:
        other_count+=1
print(char_count,space_count,num_count,other_count)

 

