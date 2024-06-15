a=input()
max_digit=""
max_value=0
temp=""
temp_value=0
for i in a:
    if i.isdigit():
        temp=temp+i
        temp_value+=1
    else:
        if temp_value>=max_value:
            max_value=temp_value
            max_digit=temp
        temp=""
        temp_value=0
if temp_value>=max_value:
    max_value=temp_value
    max_digit=temp
if max_digit=="":
    print("No digits")
else:
    print(max_digit)




