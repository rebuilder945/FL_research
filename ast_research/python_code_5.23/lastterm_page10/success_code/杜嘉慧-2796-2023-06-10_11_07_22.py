str=input()
max_list = []
flag=False
for i in range(len(str)):
    new_list = []
    for j in range(i,len(str)):
        if str[j].isdigit():
            flag=True
            new_list.append(str[j])
        else:
            break
        if len(max_list) < len(new_list):
            max_list = new_list
print("".join(max_list))
if flag==False:
    print("No digits")
