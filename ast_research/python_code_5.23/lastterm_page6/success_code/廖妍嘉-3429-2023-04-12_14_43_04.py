str = input()
a_count,n_count,s_count,o_count = 0,0,0,0
for i in str:
    if "a" <=i <= "z" or "A" <= i <= "Z":
        a_count +=1
    elif "0" <=i <= "9":
        n_count +=1
    elif i == " ":
        s_count +=1
    else:
        o_count +=1
print(a_count,n_count,s_count,o_count)
