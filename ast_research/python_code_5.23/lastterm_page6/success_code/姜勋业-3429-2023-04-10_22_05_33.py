a=input()
space=0
letter=0
number=0
other=0
for i in a:
    if "a"<=i<="z" or "A"<=i<="Z":
        letter=letter+1
    elif "0"<=i<="9":
        number=number+1
    elif i == " ":
        space=space+1
    else:
        other=other+1
print(letter,space,number,other)
