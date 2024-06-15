num=input()
chara="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrsuvwxyz!@#$%^&*()"
for c in chara:
    if c in num:
        num=num.replace(c,"*")
num_list=num.split("*")
for x in num_list[:]:
    if x=='':
        num_list.remove(x)
    else:
        pass
tin_list=[]
for x in num_list:
    tin_list.append([x,num_list.index(x),len(x)])
tin_list.sort(key=lambda x:x[2],reverse=True)
if tin_list!=[]:
    print(tin_list[0][0])
else:
    print("No digits")
