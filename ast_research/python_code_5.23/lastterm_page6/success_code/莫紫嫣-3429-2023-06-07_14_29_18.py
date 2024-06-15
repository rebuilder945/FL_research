str=input()
alpha_count,space_count,num_count,other_count=0,0,0,0
for i in str:
    if i.isalpha():
        alpha_count+=1
    elif i.isspace():
        space_count+=1
    elif i.isdigit():
        num_count+=1
    else:
        other_count+=1
print(alpha_count,space_count,num_count,other_count)


