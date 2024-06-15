str=input()
alpha_count, num_count, space_count, other_count = 0,0,0,0
for i in str:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        alpha_count+= 1
    elif i==" ":
        space_count+=1
    elif "O" <= i <= "9":
        num_count+= 1
    else:
        other_count+= 1
print(alpha_count, space_count,num_count, other_count)

