num=input()
chara="ABCDEFGHIJKLMNOPQRSTUVWXYZ\
    abcdefghijklmnopqrstuvwxyz!@#$%^&*()"
for x in chara:
    if x in num:
        num = num.replace(x,"*")
num_list=num.split("*")
for x in num_list[:]:
    if x == "":
        num_list.remove(x)
    else:
        pass
fin_list=[]
for x in num_list:
    fin_list.append([x,num_list.index(x),len(x)])
fin_list.sort(key=lambda x:(-x[2],-x[1]))
if fin_list != []:
    print(fin_list[0][0])
else:
    print("No digits")
