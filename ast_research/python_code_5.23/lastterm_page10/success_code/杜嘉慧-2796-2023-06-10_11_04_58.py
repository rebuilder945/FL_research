str=input()
max_list = []
for x in str:
    if not x.isdigit():
        print("No digits")
for i in range(len(str)):
    new_list = []
    for j in range(i+1,len(str)):
        if str[j].isdigit():
            new_list.append(str[j])
        else:
            break
        if len(max_list) < len(new_list):
            max_list = new_list
print("".join(max_list))
