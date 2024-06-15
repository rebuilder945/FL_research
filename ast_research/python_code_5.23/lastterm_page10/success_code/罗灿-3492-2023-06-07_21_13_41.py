str=input()
str_list=list(str)
ls=[]
for i in str_list:
    if str_list.count(i)==1:
        ls.append(i)
if len(ls)>0:
    print(ls[0])
else:
    print("None")
